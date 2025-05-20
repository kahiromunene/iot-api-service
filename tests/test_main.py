from fastapi.testclient import TestClient
from app import sensors

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert response.json() == {"message": "IoT API is running"}, f"Unexpected response: {response.json()}"


def test_add_and_get_sensor():
    data = {"id": 1, "temperature": 22.5, "humidity": 45.0}
    
    # Post sensor data
    post_response = client.post("/sensors/", json=data)
    assert post_response.status_code == 200, f"POST /sensors/ failed: {post_response.text}"

    # Get all sensor readings
    get_response = client.get("/sensors/")
    assert get_response.status_code == 200, f"GET /sensors/ failed: {get_response.text}"

    readings = get_response.json()
    assert any(
        r["id"] == data["id"] and r["temperature"] == data["temperature"] and r["humidity"] == data["humidity"]
        for r in readings
    ), f"Sensor data not found in response: {readings}"
