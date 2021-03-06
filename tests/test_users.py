from http import client
from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)

def test_root():
    res = client.get('/')
    print(res)
    assert res.json().get('message') == 'Hello World'

def test_create_user():
    res = client.post('/users/', json={"email": "hello123@gmail.com", "password": "password123"})
    
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'hello123@gmail.com'
    assert res.status_code == 201