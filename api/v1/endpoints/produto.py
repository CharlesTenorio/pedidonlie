from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from model.produto import ProdutoModel
from schemas.produto_schema import ProdutoSchema
from core.deps import get_session

router = APIRouter()

# Post curso 
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProdutoSchema)
async def post_produto(produto: ProdutoSchema, db: AsyncSession=Depends(get_session)):
    novo_produto = ProdutoModel(nome=produto.nome, valor = produto.valor, )
    db.add(novo_produto)
    await db.commit()
    return novo_produto

@router.get('/', response_model=List[ProdutoSchema])
async def get_produtos(db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel)
        result = await session.execute(query)
        produtos: List[ProdutoModel]=result.scalars.all()
        return produtos