from typing import Optional, List, Dict
from datetime import datetime
from pydantic import BaseModel as SCBaseModel # esse as e apra crair um apelido apra o base model pq o p sqlalchimer tem um base model para nao confudir
from schemas.pedido_schema import PedidoSchema
from schemas.produto_schema import ProdutoSchema

class PedidoSchema(SCBaseModel):
    id: Optional[int]
    id_pedido: int
    data_pagamento: datetime
    total_pago: float
    status: str
    pedido: PedidoSchema
    produtos: Optional[Dict]
    
    
    class Config:
        orm_mode = True