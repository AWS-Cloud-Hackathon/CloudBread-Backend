from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import crud
from . import models
from . import schemas
from .database import SessionLocal, engine

# 데이터베이스 초기화 (테이블 생성)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# 의존성 주입: 각 요청마다 데이터베이스 세션을 생성하고 종료
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Agency 엔드포인트


@app.get("/agencies/", response_model=List[schemas.Agency])
def read_agencies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_agencies(db, skip=skip, limit=limit)


@app.get("/agencies/{agency_id}", response_model=schemas.Agency)
def read_agency(agency_id: int, db: Session = Depends(get_db)):
    return crud.get_agency(db, agency_id=agency_id)


@app.post("/agencies/", response_model=schemas.Agency)
def create_agency(agency: schemas.AgencyCreate, db: Session = Depends(get_db)):
    return crud.create_agency(db=db, agency=agency)


@app.delete("/agencies/{agency_id}", response_model=schemas.Agency)
def delete_agency(agency_id: int, db: Session = Depends(get_db)):
    return crud.delete_agency(db=db, agency_id=agency_id)


# Member 엔드포인트


@app.get("/users/", response_model=List[schemas.Member])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/users/{user_id}", response_model=schemas.Member)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)


@app.post("/users/", response_model=schemas.Member)
def create_user(user: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.delete("/users/{user_id}", response_model=schemas.Member)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)


# Blacklist 엔드포인트


@app.get("/blacklists/", response_model=List[schemas.Blacklist])
def read_blacklists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_blacklists(db, skip=skip, limit=limit)


@app.get("/blacklists/{blacklist_id}", response_model=schemas.Blacklist)
def read_blacklist(blacklist_id: int, db: Session = Depends(get_db)):
    return crud.get_blacklist(db, blacklist_id=blacklist_id)


@app.post("/blacklists/", response_model=schemas.Blacklist)
def create_blacklist(blacklist: schemas.BlacklistCreate, db: Session = Depends(get_db)):
    return crud.create_blacklist(db=db, blacklist=blacklist)


@app.put("/blacklists/{blacklist_id}", response_model=schemas.Blacklist)
def update_blacklist(
    blacklist_id: int, blacklist: schemas.BlacklistCreate, db: Session = Depends(get_db)
):
    return crud.update_blacklist(db=db, blacklist_id=blacklist_id, blacklist=blacklist)


# Report 엔드포인트


@app.get("/reports/", response_model=List[schemas.Report])
def read_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_reports(db, skip=skip, limit=limit)


@app.get("/reports/{report_id}", response_model=schemas.Report)
def read_report(report_id: int, db: Session = Depends(get_db)):
    return crud.get_report(db, report_id=report_id)


@app.post("/reports/", response_model=schemas.Report)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    return crud.create_report(db=db, report=report)


@app.delete("/reports/{report_id}", response_model=schemas.Report)
def delete_report(report_id: int, db: Session = Depends(get_db)):
    return crud.delete_report(db=db, report_id=report_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
