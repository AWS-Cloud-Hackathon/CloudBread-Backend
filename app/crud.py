from sqlalchemy.orm import Session
from . import models, schemas

# Agency CRUD


# 전체 수요 기관 조회
def get_agencies(db: Session):
    # return db.query(models.Agency).offset(skip).limit(limit).all()
    return db.query(models.Agency).all()


# 특정 수요 기관 조회
def get_agency(db: Session, agency_id: int):
    return db.query(models.Agency).filter(models.Agency.id == agency_id).first()


# 수요 기관 추가
def create_agency(db: Session, agency: schemas.AgencyCreate):
    db_agency = models.Agency(**agency.dict())
    db.add(db_agency)
    db.commit()
    db.refresh(db_agency)
    return db_agency


# 특정 수요 기관 삭제
def delete_agency(db: Session, agency_id: int):
    db_agency = get_agency(db, agency_id)
    if db_agency:
        db.delete(db_agency)
        db.commit()
    return db_agency


# Member CRUD


# 전체 유저 조회
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()


# 특정 유저 조회
def get_user(db: Session, user_id: int):
    return db.query(models.Member).filter(models.Member.id == user_id).first()


# 유저 추가
def create_user(db: Session, user: schemas.MemberCreate):
    db_user = models.Member(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 특정 유저 삭제
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def get_agencies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Agency).offset(skip).limit(limit).all()


def get_agency(db: Session, agency_id: int):
    return db.query(models.Agency).filter(models.Agency.id == agency_id).first()


def create_agency(db: Session, agency: schemas.AgencyCreate):
    db_agency = models.Agency(**agency.dict())
    db.add(db_agency)
    db.commit()
    db.refresh(db_agency)
    return db_agency


def delete_agency(db: Session, agency_id: int):
    db_agency = get_agency(db, agency_id)
    if db_agency:
        db.delete(db_agency)
        db.commit()
    return db_agency


# Member CRUD


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.Member).filter(models.Member.id == user_id).first()


def create_user(db: Session, user: schemas.MemberCreate):
    db_user = models.Member(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# Blacklist CRUD


def get_blacklists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blacklist).offset(skip).limit(limit).all()


def get_blacklist(db: Session, blacklist_id: int):
    return (
        db.query(models.Blacklist).filter(models.Blacklist.id == blacklist_id).first()
    )


def create_blacklist(db: Session, blacklist: schemas.BlacklistCreate):
    db_blacklist = models.Blacklist(**blacklist.dict())
    db.add(db_blacklist)
    db.commit()
    db.refresh(db_blacklist)
    return db_blacklist


def update_blacklist(
    db: Session, blacklist_id: int, blacklist: schemas.BlacklistCreate
):
    db_blacklist = get_blacklist(db, blacklist_id)
    if db_blacklist:
        for key, value in blacklist.dict().items():
            setattr(db_blacklist, key, value)
        db.commit()
        db.refresh(db_blacklist)
    return db_blacklist


# Report CRUD


def get_reports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Report).offset(skip).limit(limit).all()


def get_report(db: Session, report_id: int):
    return db.query(models.Report).filter(models.Report.id == report_id).first()


def create_report(db: Session, report: schemas.ReportCreate):
    db_report = models.Report(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


def delete_report(db: Session, report_id: int):
    db_report = get_report(db, report_id)
    if db_report:
        db.delete(db_report)
        db.commit()
    return db_report
