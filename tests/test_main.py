def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the IoT API"}

def test_add_and_get_sensor():
    data = {"id": 1, "temperature": 22.5, "humidity": 45.0}
    response = client.post("/sensors/", json=data)
    # Temporarily check for 500 to see error details (or skip for now)
    assert response.status_code == 200, f"POST /sensors/ failed: {response.text}"

    get_response = client.get("/sensors/")
    assert get_response.status_code == 200
    assert data in get_response.json()
