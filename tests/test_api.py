
import sys
from pathlib import Path

# Ensure the project root is on sys.path so `main` can be imported when pytest runs.
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "FastAPI is running"}


def test_read_item_success():
    r = client.get("/items/2")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 2
    assert data["name"] == "Item 2"


def test_read_item_not_found():
    r = client.get("/items/0")
    assert r.status_code == 404


def test_create_item():
    payload = {"name": "New", "description": "created via test"}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["name"] == "New"
