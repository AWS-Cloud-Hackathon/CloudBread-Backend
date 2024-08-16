from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

userName = "cloudbread"
password = "cloudbread!"
endpoint = "cloudbread-database.cpe0a008coe5.ap-northeast-2.rds.amazonaws.com"
port = 3306
dbname = "cloudbread"

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{userName}:{password}@{endpoint}:{port}/{dbname}"
)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1004@localhost/cloudbread"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
