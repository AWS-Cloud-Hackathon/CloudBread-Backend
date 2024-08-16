from sqlalchemy import Column
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Agency(Base):
    __tablename__ = "agency"

    id = Column(int, primary_key=True, index=True, autoincrement=True)
    name = Column(str, nullable=False)
    category = Column(int, nullable=False)
    username = Column(str, unique=True, nullable=False)
    password = Column(str, nullable=False)
    date_created = Column(datetime, default=datetime, nullable=False)
    date_modified = Column(
        datetime, default=datetime, onupdate=datetime, nullable=False
    )

    blacklists = relationship("Blacklist", back_populates="agency")


class Member(Base):
    __tablename__ = "member"

    id = Column(int, primary_key=True, index=True, autoincrement=True)
    username = Column(str, unique=True, nullable=False)
    password = Column(str, nullable=False)
    date_created = Column(datetime, default=datetime, nullable=False)
    date_modified = Column(
        datetime, default=datetime, onupdate=datetime, nullable=False
    )


class Blacklist(Base):
    __tablename__ = "blacklist"

    id = Column(int, primary_key=True, index=True, autoincrement=True)
    agency_id = Column(int, ForeignKey("agency.id"), nullable=False)
    purpose_id = Column(int, nullable=False)
    target = Column(str, nullable=False)
    state = Column(int, nullable=False)
    date_start = Column(datetime, nullable=False)
    date_end = Column(datetime, nullable=False)
    car_category = Column(str, nullable=False)
    car_model = Column(str, nullable=False)
    car_color = Column(str, nullable=False)
    date_created = Column(datetime, default=datetime, nullable=False)
    date_modified = Column(
        datetime, default=datetime, onupdate=datetime, nullable=False
    )

    agency = relationship("Agency", back_populates="blacklists")


class Report(Base):
    __tablename__ = "report"

    id = Column(int, primary_key=True, index=True, autoincrement=True)
    blacklist_id = Column(int, ForeignKey("blacklist.id"), nullable=False)
    member_id = Column(int, ForeignKey("member.id"), nullable=False)
    page = Column(int, nullable=False)
    date_find = Column(datetime, nullable=False)
    gps_x = Column(float, nullable=False)
    gps_y = Column(float, nullable=False)
