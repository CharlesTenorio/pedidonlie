from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    valor = Column(Float)

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"))
    data_pedido = Column(DateTime(timezone=True), server_default=func.now())
    total = Column(Float)

    cliente = relationship("Cliente", back_populates="pedidos")
    detalhes = relationship("DetalhePedido", back_populates="pedido")

class DetalhePedido(Base):
    __tablename__ = "detalhes_pedidos"

    id = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey("pedidos.id"))
    id_produto = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    valor = Column(Float)
    subtotal = Column(Float)

    pedido = relationship("Pedido", back_populates="detalhes")
    produto = relationship("Produto")

Base.metadata.create_all(bind=engine)