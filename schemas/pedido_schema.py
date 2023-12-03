from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel as SCBaseModel # esse as e apra crair um apelido apra o base model pq o p sqlalchimer tem um base model para nao confudir
from schemas.cliente_schema import ClienteSchema
from schemas.produto_schema import ProdutoSchema



class PedidoSchema(SCBaseModel):
    id: Optional[int]
    id_cliente: int
    data_pedido: datetime
    total: float
    status: str
    cliente: ClienteSchema
    detalhes: List["DetalhePedidoSchema"]
    
    class Config:
        orm_mode = True

class DetalhePedidoSchema(SCBaseModel):
    id: Optional[int]
    id_pedido: int
    id_produto: int
    quantidade: int
    valor: float
    subtotal: float
    pedido: PedidoSchema
    produto: ProdutoSchema
    
    class Config:
        orm_mode = True