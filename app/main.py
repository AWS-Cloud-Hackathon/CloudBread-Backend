from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# Database dependency
# Assume that you have a function `get_db()` defined elsewhere which provides the `db` session
# e.g., db: Session = Depends(get_db)

# ----------------------------------------
# Agency Endpoints
# ----------------------------------------


@app.get("/")
def read_fastapi(db: Session = Depends(get_db)):
    return {"status": "success", "message": "Hello World"}


@app.get("/agencies/", response_model=list[schemas.Agency])
def read_agencies(db: Session = Depends(get_db)):
    agencies = crud.get_agencies(db)
    return agencies


@app.post("/agencies/", response_model=schemas.Agency)
def create_agency(agency: schemas.AgencyCreate, db: Session = Depends(get_db)):
    return crud.create_agency(db=db, agency=agency)


@app.get("/agencies/{id}", response_model=schemas.Agency)
def read_agency(id: int, db: Session = Depends(get_db)):
    agency = crud.get_agency(db, agency_id=id)
    if agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")
    return agency


@app.delete("/agencies/{id}", response_model=schemas.Agency)
def delete_agency(id: int, db: Session = Depends(get_db)):
    agency = crud.delete_agency(db, agency_id=id)
    if agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")
    return agency


# ----------------------------------------
# Member Endpoints
# ----------------------------------------


@app.get("/users/", response_model=List[schemas.Member])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/", response_model=schemas.Member)
def create_user(user: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users/{id}", response_model=schemas.Member)
def read_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{id}", response_model=schemas.Member)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id=id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ----------------------------------------
# Blacklist Endpoints
# ----------------------------------------


@app.get("/blacklists/", response_model=List[schemas.Blacklist])
def read_blacklists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blacklists = crud.get_blacklists(db, skip=skip, limit=limit)
    return blacklists


@app.post("/blacklists/", response_model=schemas.Blacklist)
def create_blacklist(blacklist: schemas.BlacklistCreate, db: Session = Depends(get_db)):
    return crud.create_blacklist(db=db, blacklist=blacklist)


@app.get("/blacklists/{id}", response_model=schemas.Blacklist)
def read_blacklist(id: int, db: Session = Depends(get_db)):
    blacklist = crud.get_blacklist(db, blacklist_id=id)
    if blacklist is None:
        raise HTTPException(status_code=404, detail="Blacklist not found")
    return blacklist


@app.put("/blacklists/{id}", response_model=schemas.Blacklist)
def update_blacklist(
    id: int, blacklist: schemas.BlacklistCreate, db: Session = Depends(get_db)
):
    updated_blacklist = crud.update_blacklist(db, blacklist_id=id, blacklist=blacklist)

    if updated_blacklist is None:
        raise HTTPException(status_code=404, detail="Blacklist not found")
    return updated_blacklist


# ----------------------------------------
# Report Endpoints
# ----------------------------------------


@app.get("/reports/", response_model=List[schemas.Report])
def read_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reports = crud.get_reports(db, skip=skip, limit=limit)
    return reports


@app.post("/reports/", response_model=schemas.Report)
def create_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    return crud.create_report(db=db, report=report)


@app.get("/reports/{id}", response_model=schemas.Report)
def read_report(id: int, db: Session = Depends(get_db)):
    report = crud.get_report(db, report_id=id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report


@app.delete("/reports/{id}", response_model=schemas.Report)
def delete_report(id: int, db: Session = Depends(get_db)):
    report = crud.delete_report(db, report_id=id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report
