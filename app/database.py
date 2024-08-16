from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

userName = ""
password = ""
endpoint = ""
port = 3306
dbname = ""

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{userName}:{password}@{endpoint}:{port}/{dbname}"
)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
