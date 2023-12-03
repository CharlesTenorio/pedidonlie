import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from model.pedido import PedidoModel
import pika

async def get_orders_to_process(db: AsyncSession):
    async with db as session:
        # Filtrar todos os pedidos com status "em aberto"
        query = select(PedidoModel).filter(PedidoModel.status == "em aberto")
        result = await session.execute(query)
        orders_to_process = result.scalars().all()

        # Preparar os dados para enviar para a fila
        details_to_send = [{"id": order.id, "valor": order.total} for order in orders_to_process]

        return details_to_send

async def send_orders_to_rabbitmq(db: AsyncSession):
    orders_to_process = await get_orders_to_process(db)

    for order_details in orders_to_process:
        # Enviar os detalhes para o RabbitMQ
        send_to_rabbitmq(order_details)

        # Alterar o status do pedido para "enviado para processamento"
        await update_order_status(db, order_details["id"], "enviado para processamento")

async def process_orders_periodically(db: AsyncSession):
    while True:
        await send_orders_to_rabbitmq(db)
        await asyncio.sleep(120)  # Aguardar 2 minutos

def send_to_rabbitmq(data):
    # Configurar a conexão com o RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar a fila (substitua 'pagamento_fila' pelo nome desejado)
    channel.queue_declare(queue='pagamento_fila')

    # Enviar os dados para a fila
    channel.basic_publish(exchange='', routing_key='pagamento_fila', body=str(data))

    # Fechar a conexão
    connection.close()



async def update_order_status(db: AsyncSession, order_id: int, new_status: str):
    async with db as session:
        order = await session.get(PedidoModel, order_id)
        if order:
            order.status = new_status
            await session.commit()
