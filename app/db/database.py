from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy import event
from app.models import *

engine = create_engine('sqlite:///./database.db', echo=True)

@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")

def init_db():
    SQLModel.metadata.create_all(engine)
    
def get_db():
    with Session(engine) as session:
        yield session
        
