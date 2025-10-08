from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True

class CursoSchemaCreate(SCBaseModel):
    titulo: str
    aulas: int
    horas: int
   
    class Config:
        orm_mode = True

#posso criar quantos schemas eu quiser, para diferentes finalidades, num mesmo model
