from core.configs import settings
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class ProdutoModel(settings.DBBaseModel):
    __tablename__ = 'produtos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome : str = Column(String(50), unique=True)
    valor: float = Column(DECIMAL(precision=10, scale=2))

class ClienteModel(settings.DBBaseModel):
    __tablename__ = 'clientes'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(50), unique=True)

class PedidoModel(settings.DBBaseModel):
    __tablename__ = 'pedidos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente: int = Column(Integer, ForeignKey('clientes.id'))
    data_pedido: datetime = Column(DateTime, default=datetime.utcnow)
    total: float = Column(DECIMAL(precision=10, scale=2))

    cliente = relationship('ClienteModel', back_populates='pedidos')
    detalhes = relationship('DetalhePedidoModel', back_populates='pedido')

class DetalhePedidoModel(settings.DBBaseModel):
    __tablename__ = 'detalhes_pedidos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido: int = Column(Integer, ForeignKey('pedidos.id'))
    id_produto: int = Column(Integer, ForeignKey('produtos.id'))
    quantidade: int = Column(Integer)
    valor: float = Column(DECIMAL(precision=10, scale=2))
    subtotal: float = Column(DECIMAL(precision=10, scale=2))

    pedido = relationship('PedidoModel', back_populates='detalhes')
    produto = relationship('ProdutoModel')

# Adicione a relação na classe ClienteModel
ClienteModel.pedidos = relationship('PedidoModel', back_populates='cliente')