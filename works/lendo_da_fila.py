import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from model.pedido import PedidoModel
from model.pagamento import PagamentodoModel
import pika
from datetime import datetime, timedelta

async def read_and_save_from_queue(db: AsyncSession):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar a fila (substitua 'minha_fila' pelo nome desejado)
    channel.queue_declare(queue='minha_fila')

    def callback(ch, method, properties, body):
        data = eval(body.decode())  # Certifique-se de que a serialização/deserialização está correta
        asyncio.create_task(save_to_database(db, data))

    # Configurar o consumo da fila
    channel.basic_consume(queue='minha_fila', on_message_callback=callback, auto_ack=True)

    # Iniciar o consumo
    channel.start_consuming()

async def save_to_database(db: AsyncSession, data):
    async with db as session:
        try:
            # Criar o objeto PagamentodoModel
            pagamento = PagamentodoModel(
                id_pedido=data['id_pedido'],
                data_pagamento=datetime.utcnow(),
                total_pago=data['total'],
                status="pedido pago"
            )

            # Salvar no banco de dados
            session.add(pagamento)
            await session.commit()

            # Atualizar o status do pedido para "pago"
            await update_pedido_status(db, data['id_pedido'], "pago")

        except Exception as e:
            print(f"Erro ao salvar no banco de dados: {e}")

async def update_pedido_status(db: AsyncSession, pedido_id: int, new_status: str):
    async with db as session:
        pedido = await session.get(PedidoModel, pedido_id)
        if pedido:
            pedido.status = new_status
            await session.commit()