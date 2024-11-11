from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


server_name = "DESKTOP-O79B368\\SQLEXPRESS"
database_name = "telefon_rehberi"

# MSSQL bağlantısı
mssql_dp_url = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
# SQLAlchemy engine oluşturma
engine = create_engine(mssql_dp_url,connect_args={
         "chech_same_thread": False})

SessionLocal = sessionmaker(bind = engine, autocommit=False, autoflush=False,)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
