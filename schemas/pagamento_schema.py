from decimal import Decimal
from typing import Optional
from datetime import datetime
from pydantic import BaseModel as SCBaseModel # esse as e apra crair um apelido apra o base model pq o p sqlalchimer tem um base model para nao confudir
from schemas.pedido_schema import PedidoSchema
from schemas.produto_schema import ProdutoSchema

class PagamentoSchema(SCBaseModel):
    id: Optional[int]
    id_pedido: int
    data_pagamento: datetime
    total_pago: Decimal
    status: str
   
    class Config:
        orm_mode = True
        
