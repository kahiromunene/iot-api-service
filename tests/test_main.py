from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "IoT API is running"}

def test_add_and_get_sensor():
    data = {"id": 1, "temperature": 22.5, "humidity": 45.0}
    response = client.post("/sensors/", json=data)
    assert response.status_code == 200
    assert response.json() == data

    get_response = client.get("/sensors/")
    assert get_response.status_code == 200
    assert data in get_response.json()

