from core.configs import settings
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ClienteModel(settings.DBBaseModel):
    __tablename__ = 'clientes'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(50), unique=True)

    # Não importe PedidoModel diretamente aqui

    # Importe PedidoModel no escopo da função onde você precisar usar
    # from model.pedido import PedidoModel

    pedidos = relationship('PedidoModel', back_populates='cliente')