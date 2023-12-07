from core.configs import settings
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class PagamentodoModel(settings.DBBaseModel):
    __tablename__ = 'pagamento'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido: int = Column(Integer, ForeignKey('pedidos.id'))
    data_pagamento: datetime = Column(DateTime, default=datetime.utcnow)
    total_pago: float = Column(DECIMAL(precision=10, scale=2))
    status : str = Column(String(50))
   