from typing import Any, Dict, Optional, Tuple
from sqlmodel import Field, SQLModel
from werkzeug.security import check_password_hash, generate_password_hash


class Livros(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    titulo: Optional[str]
    autor: Optional[str]


class Autores(SQLModel, table=True):
        id: Optional[int] = Field(primary_key=True)
        nome: Optional[str]
        email: Optional[str]
        nome_do_livro: Optional[str]

class User(SQLModel, table=True):
        id: Optional[int] = Field(primary_key=True)
        nome: Optional[str]
        email: Optional[str] = Field(unique=True)
        password: Optional[str] = Field(unique=False)
