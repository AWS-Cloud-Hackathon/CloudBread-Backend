import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from main import get_db
from main import app

# 테스트를 위한 SQLite 메모리 데이터베이스 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 테스트용 DB 연결 의존성 설정
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    # 테스트 데이터베이스에 필요한 테이블을 생성합니다.
    Base.metadata.create_all(bind=engine)
    yield
    # 테스트 후 데이터베이스를 정리합니다.
    Base.metadata.drop_all(bind=engine)


# Agency API 테스트


def test_create_agency():
    response = client.post(
        "/agencies/",
        json={
            "name": "Agency 1",
            "category": 1,
            "username": "agency1",
            "password": "pass123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Agency 1"
    assert data["category"] == 1
    assert data["username"] == "agency1"


def test_read_agencies():
    response = client.get("/agencies/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_read_agency():
    response = client.get("/agencies/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Agency 1"


def test_delete_agency():
    response = client.delete("/agencies/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Agency 1"


# Member API 테스트


def test_create_user():
    response = client.post("/users/", json={"username": "user1", "password": "pass123"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "user1"


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "user1"


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "user1"


# Blacklist API 테스트


def test_create_blacklist():
    response = client.post(
        "/blacklists/",
        json={
            "agency_id": 1,
            "purpose_id": 1,
            "target": "target1",
            "state": 1,
            "date_start": "2024-01-01T00:00:00",
            "date_end": "2024-12-31T23:59:59",
            "car_category": "SUV",
            "car_model": "Model X",
            "car_color": "Black",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["target"] == "target1"


def test_read_blacklists():
    response = client.get("/blacklists/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_read_blacklist():
    response = client.get("/blacklists/1")
    assert response.status_code == 200
    data = response.json()
    assert data["target"] == "target1"


def test_update_blacklist():
    response = client.put(
        "/blacklists/1",
        json={
            "agency_id": 1,
            "purpose_id": 1,
            "target": "updated_target",
            "state": 2,
            "date_start": "2024-01-01T00:00:00",
            "date_end": "2024-12-31T23:59:59",
            "car_category": "SUV",
            "car_model": "Model X",
            "car_color": "Black",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["target"] == "updated_target"


# Report API 테스트


def test_create_report():
    response = client.post(
        "/reports/",
        json={
            "blacklist_id": 1,
            "member_id": 1,
            "page": 1,
            "date_find": "2024-01-15T12:00:00",
            "gps_x": 37.7749,
            "gps_y": -122.4194,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1


def test_read_reports():
    response = client.get("/reports/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_read_report():
    response = client.get("/reports/1")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1


def test_delete_report():
    response = client.delete("/reports/1")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1
