from fastapi import APIRouter
from api.v1.endpoints import cliente


# aqui onde junta todas as apis

api_router = APIRouter()
api_router.include_router(cliente.router, prefix='/clientes', tags=["clientes"])

#/api/v1/cursos 
           