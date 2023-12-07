from core.configs import settings
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey, JSON

from sqlalchemy.orm import relationship
from datetime import datetime

class PedidoModel(settings.DBBaseModel):
    __tablename__ = 'pedidos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente: int = Column(Integer, ForeignKey('clientes.id'))
    data_pedido: datetime = Column(DateTime, default=datetime.utcnow)
    total: float = Column(DECIMAL(precision=10, scale=2))
    descricao: str=Column(String(100))
    statuspedido: str = Column(String(30))
    
