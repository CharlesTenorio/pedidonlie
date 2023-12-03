from core.configs import settings
from sqlalchemy import Column, Integer, String, DECIMAL


class ProdutoModel(settings.DBBaseModel):
    __tablename__ = 'produtos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome : str = Column(String(50), unique=True)
    valor: float = Column(DECIMAL(precision=10, scale=2))
