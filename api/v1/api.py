from fastapi import APIRouter
from api.v1.endpoints import cliente
from api.v1.endpoints import produto
from api.v1.endpoints import pedido
from api.v1.endpoints import pagamento


# aqui onde junta todas as apis

api_router = APIRouter()
api_router.include_router(cliente.router, prefix='/clientes', tags=["clientes"])
api_router.include_router(produto.router, prefix='/produtos', tags=["produtos"])
api_router.include_router(pedido.router, prefix='/pedidos', tags=["predidos"])
api_router.include_router(pagamento.router, prefix='/pagamentos', tags=["pagamentos"])



#/api/v1/cursos 
           