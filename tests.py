import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

def test_counter():
    response = client.get("/counter")
    assert response.status_code == 200
    assert response.text == "1"

    response = client.get("/counter")
    assert response.status_code == 200
    assert response.text == "2"

def test_method_post():
    response = client.post("/method")
    assert response.status_code == 201
    assert response.json() == {"method": "POST"}
