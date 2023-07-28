from typing import Any
from sqlmodel import SQLModel, Session, create_engine, select
from utils.dot_env import DotEnvEnum
from utils.settings import Settings

engine = create_engine(
    url=Settings.get(
        DotEnvEnum.DATABASE_URI.value,
    ),
    echo=True,
)
SQLModel.metadata.create_all(engine)


class Database:
    def get_one(self, statement):
        with Session(engine) as session:
            return session.exec(statement).first()
    
    def get_all(self, statement):
        with Session(engine) as session:
            return session.exec(statement).all()

    def run_insert(self, object_model: Any):
        with Session(engine) as session:
            session.add(object_model)
            session.commit()

    def run_delete(self, object_model: Any):
        with Session(engine) as session:
            session.delete(object_model)
            session.commit()

    def run_update(self, object_model: Any):
        with Session(engine) as session:
            session.add(object_model)
            session.commit()
