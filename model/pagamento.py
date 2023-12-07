from core.configs import settings
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from model.produto import ProdutoModel
from model.cliente import ClienteModel



class PagamentodoModel(settings.DBBaseModel):
    __tablename__ = 'pagamento'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido: int = Column(Integer, ForeignKey('pedido.id'))
    data_pagamento: datetime = Column(DateTime, default=datetime.utcnow)
    total_pago: float = Column(DECIMAL(precision=10, scale=2))
    status : str = Column(String(50))


def create_payment(session, db, id_pedido, total_pago, status):
    payment = PagamentodoModel(id_pedido=id_pedido, total_pago=total_pago, status=status)
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment

# Função para listar pagamentos
def list_payments(session, db, id_pedido=0):
    if id_pedido:
        return session.query(PagamentodoModel).filter_by(id_pedido=id_pedido).all()
    else:
        return session.query(PagamentodoModel).all()

   