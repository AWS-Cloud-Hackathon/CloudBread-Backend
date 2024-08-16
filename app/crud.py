from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models
from . import schemas

# Agency CRUD


def get_agencies(db: Session, skip: int = 0, limit: int = 10):
    agencies = db.query(models.Agency).offset(skip).limit(limit).all()
    if not agencies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No agencies found"
        )
    return agencies


def get_agency(db: Session, agency_id: int):
    agency = db.query(models.Agency).filter(models.Agency.id == agency_id).first()
    if agency is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found"
        )
    return agency


def create_agency(db: Session, agency: schemas.AgencyCreate):
    db_agency = models.Agency(**agency.dict())
    try:
        db.add(db_agency)
        db.commit()
        db.refresh(db_agency)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating agency"
        )
    return db_agency


def delete_agency(db: Session, agency_id: int):
    agency = get_agency(db, agency_id)
    if agency:
        db.delete(agency)
        try:
            db.commit()
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting agency"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found"
        )
    return agency


# Member CRUD


def get_users(db: Session, skip: int = 0, limit: int = 10):
    users = db.query(models.Member).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No users found"
        )
    return users


def get_user(db: Session, user_id: int):
    user = db.query(models.Member).filter(models.Member.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def create_user(db: Session, user: schemas.MemberCreate):
    db_user = models.Member(**user.dict())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user"
        )
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        try:
            db.commit()
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting user"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


# Blacklist CRUD


def get_blacklists(db: Session, skip: int = 0, limit: int = 10):
    blacklists = db.query(models.Blacklist).offset(skip).limit(limit).all()
    if not blacklists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No blacklists found"
        )
    return blacklists


def get_blacklist(db: Session, blacklist_id: int):
    blacklist = (
        db.query(models.Blacklist).filter(models.Blacklist.id == blacklist_id).first()
    )
    if blacklist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blacklist not found"
        )
    return blacklist


def create_blacklist(db: Session, blacklist: schemas.BlacklistCreate):
    db_blacklist = models.Blacklist(**blacklist.dict())
    try:
        db.add(db_blacklist)
        db.commit()
        db.refresh(db_blacklist)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating blacklist"
        )
    return db_blacklist


def update_blacklist(
    db: Session, blacklist_id: int, blacklist: schemas.BlacklistCreate
):
    db_blacklist = get_blacklist(db, blacklist_id)
    if db_blacklist:
        for key, value in blacklist.dict().items():
            setattr(db_blacklist, key, value)
        try:
            db.commit()
            db.refresh(db_blacklist)
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error updating blacklist",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blacklist not found"
        )
    return db_blacklist


# Report CRUD


def get_reports(db: Session, skip: int = 0, limit: int = 10):
    reports = db.query(models.Report).offset(skip).limit(limit).all()
    if not reports:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No reports found"
        )
    return reports


def get_report(db: Session, report_id: int):
    report = db.query(models.Report).filter(models.Report.id == report_id).first()
    if report is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report not found"
        )
    return report


def create_report(db: Session, report: schemas.ReportCreate):
    db_report = models.Report(**report.dict())
    try:
        db.add(db_report)
        db.commit()
        db.refresh(db_report)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating report"
        )
    return db_report


def delete_report(db: Session, report_id: int):
    report = get_report(db, report_id)
    if report:
        db.delete(report)
        try:
            db.commit()
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting report"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report not found"
        )
    return report
