
from typing import Optional

from pydantic import BaseModel as SCBaseModel # esse as e apra crair um apelido apra o base model pq o p sqlalchimer tem um base model para nao confudir

class ClienteSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    
    class Config:
        orm_mode = True
