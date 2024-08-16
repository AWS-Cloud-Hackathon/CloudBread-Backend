from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AgencyBase(BaseModel):
    name: str
    category: int
    username: str


class AgencyCreate(AgencyBase):
    password: str


class Agency(AgencyBase):
    id: int
    date_created: datetime
    date_modified: datetime

    class Config:
        from_attributes = True


class MemberBase(BaseModel):
    username: str


class MemberCreate(MemberBase):
    password: str


class Member(MemberBase):
    id: int
    date_created: datetime
    date_modified: datetime

    class Config:
        from_attributes = True


class BlacklistBase(BaseModel):
    agency_id: int
    purpose_id: int
    target: str
    state: int
    date_start: datetime
    date_end: datetime
    car_category: str
    car_model: str
    car_color: str


class BlacklistCreate(BlacklistBase):
    pass


class Blacklist(BlacklistBase):
    id: int
    date_created: datetime
    date_modified: datetime
    agency: Optional[Agency] = None

    class Config:
        from_attributes = True


class ReportBase(BaseModel):
    blacklist_id: int
    member_id: int
    page: int
    date_find: datetime
    gps_x: float
    gps_y: float


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int

    class Config:
        from_attributes = True
