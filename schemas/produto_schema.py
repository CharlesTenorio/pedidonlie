
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel as SCBaseModel # esse as e apra crair um apelido apra o base model pq o p sqlalchimer tem um base model para nao confudir

class ProdutoSchema(SCBaseModel):
    id: Optional[int]
    nome : str 
    valor: float 
    
    class Config:
        orm_mode = True

