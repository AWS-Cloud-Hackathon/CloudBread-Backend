from sqlalchemy import Column, Integer, DateTime, Float, VARCHAR
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Agency(Base):
    __tablename__ = "agency"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(VARCHAR(45), nullable=False)
    category = Column(Integer, nullable=False)
    username = Column(VARCHAR(45), unique=True, nullable=False)
    password = Column(VARCHAR(45), nullable=False)
    date_created = Column(DateTime, default=datetime, nullable=False)
    date_modified = Column(
        DateTime, default=datetime, onupdate=datetime, nullable=False
    )

    blacklists = relationship("Blacklist", back_populates="agency")


class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(VARCHAR(45), unique=True, nullable=False)
    password = Column(VARCHAR(45), nullable=False)
    date_created = Column(DateTime, default=datetime, nullable=False)
    date_modified = Column(
        DateTime, default=datetime, onupdate=datetime, nullable=False
    )


class Blacklist(Base):
    __tablename__ = "blacklist"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    agency_id = Column(Integer, ForeignKey("agency.id"), nullable=False)
    purpose_id = Column(Integer, nullable=False)
    target = Column(VARCHAR(45), nullable=False)
    state = Column(Integer, nullable=False)
    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    car_category = Column(VARCHAR(45), nullable=False)
    car_model = Column(VARCHAR(45), nullable=False)
    car_color = Column(VARCHAR(45), nullable=False)
    date_created = Column(DateTime, default=datetime, nullable=False)
    date_modified = Column(
        DateTime, default=datetime, onupdate=datetime, nullable=False
    )

    agency = relationship("Agency", back_populates="blacklists")


class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    blacklist_id = Column(Integer, ForeignKey("blacklist.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("member.id"), nullable=False)
    page = Column(Integer, nullable=False)
    date_find = Column(DateTime, nullable=False)
    gps_x = Column(Float, nullable=False)
    gps_y = Column(Float, nullable=False)
