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
        produtos: List[ProdutoModel]= result.scalars().all()
        return produtos

# pega somente um cliente passado o id do cliente

@router.get('/{produto_id}', response_model=ProdutoSchema, status_code=status.HTTP_200_OK)
async def get_produto(produto_id: int, db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel).filter(ProdutoModel.id==produto_id)
        result = await session.execute(query)
        produto =result.scalar_one_or_none()
        if produto:
             return produto
        else:
            raise HTTPException(detail='produto não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND) 

# atauloiza um cliente pelasso id, e nome 
@router.put('/{produto_id}', response_model=ProdutoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_cliente(produto_id: int, cliente: ProdutoSchema, db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel).filter(ProdutoModel.id==produto_id)
        result = await session.execute(query)
        produto_up =result.scalar_one_or_none()
        if produto_up:
            produto_up.nome=cliente.nome
            await session.commit()
            return produto_up
            
        else:
            raise HTTPException(detail='produto não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND) 

# deleta um cliente passado o id do cliente
@router.delete('/{produto_id}', status_code=status.HTTP_204_NO_CONTENT)
async def put_cliente(produto_id: int,  db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProdutoModel).filter(ProdutoModel.id==produto_id)
        result = await session.execute(query)
        produto_del =result.scalar_one_or_none()
        if produto_del:
           
            await session.delete(produto_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
            
        else:
            raise HTTPException(detail='produto não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND) 

    