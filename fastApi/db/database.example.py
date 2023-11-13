from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "DIALECT+DRIVER://USER:PWD@HOST/DATATABLE"
engine = create_engine(database_url, pool_recycle=PORT, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()
