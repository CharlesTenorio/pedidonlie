from typing import Optional, List, Dict
from datetime import datetime
from pydantic import BaseModel as SCBaseModel


class PedidoSchema(SCBaseModel):
    id: Optional[int]
    id_cliente: int
    data_pedido: datetime
    total: float
    descricao: Optional[str]
    statuspedido: Optional[str]
    produtos: Optional[Dict]
  
    class Config:
        orm_mode = True

# Adicione esta linha para atualizar as referências antes da validação


