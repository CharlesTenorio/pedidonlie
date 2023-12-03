from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from model.pedido import PedidoModel

from schemas.pedido_schema import PedidoSchema
from core.deps import get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PedidoSchema)
async def post_pedido(pedido: PedidoSchema, db: AsyncSession = Depends(get_session)):
    try:
        async with db as session:
            # Criar o pedido
            novo_pedido = PedidoModel(
                id_cliente=pedido.id_cliente,
                data_pedido=pedido.data_pedido,
                total=pedido.total,
                descricao=pedido.descricao,
                statuspedido=pedido.statuspedido
                
            )
            session.add(novo_pedido)
            await session.commit()
            await session.refresh(novo_pedido)

            # Adicionar detalhes do pedido
           

            return novo_pedido

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get('/', response_model=List[PedidoSchema])
async def get_pedidos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PedidoModel)
        result = await session.execute(query)
        pedidos: List[PedidoModel] = result.scalars.all()
        return pedidos
