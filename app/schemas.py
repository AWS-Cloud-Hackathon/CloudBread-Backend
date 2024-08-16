from pydantic import BaseModel
from datetime import datetime

# 1. Agency 스키마


# Agency 베이스 모델
class AgencyBase(BaseModel):
    name: str
    category: int
    username: str


# Agency 생성용 모델
class AgencyCreate(AgencyBase):
    password: str


# Agency 응답용 모델
class Agency(AgencyBase):
    id: int
    date_created: datetime
    date_modified: datetime

    class Config:
        from_attributes = True


# 2. Member 스키마


# Member 베이스 모델
class MemberBase(BaseModel):
    username: str


# Member 생성용 모델
class MemberCreate(MemberBase):
    password: str


# Member 응답용 모델
class Member(MemberBase):
    id: int
    date_created: datetime
    date_modified: datetime

    class Config:
        from_attributes = True


# 3. Blacklist 스키마


# Blacklist 베이스 모델
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


# Blacklist 생성용 모델
class BlacklistCreate(BlacklistBase):
    pass


# Blacklist 응답용 모델
class Blacklist(BlacklistBase):
    id: int
    date_created: datetime
    date_modified: datetime

    class Config:
        from_attributes = True


# 4. Report 스키마


# Report 베이스 모델
class ReportBase(BaseModel):
    blacklist_id: int
    member_id: int
    page: int
    date_find: datetime
    gps_x: float
    gps_y: float


# Report 생성용 모델
class ReportCreate(ReportBase):
    pass


# Report 응답용 모델
class Report(ReportBase):
    id: int

    class Config:
        from_attributes = True
