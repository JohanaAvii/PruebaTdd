from main import is_prime
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_isPrime1():
    response = client.get("/is_prime/2")
    assert response.status_code == 200
    assert response.json() == {"changed": False, "msg": "Es primo"}   

def test_read_isPrime2():
    response = client.get("/is_prime/-2")
    assert response.status_code == 200
    assert response.json() == {"changed": True, "msg": "No es primo"} 

def test_read_isPrime3():
    response = client.get("/is_prime/f")
    assert response.status_code == 200
    assert response.json() == {"detail":[{"loc":["path","is_primo_id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}   

def test_read_isPrime4():
    response = client.get("/is_prime/1")
    assert response.status_code == 200
    assert response.json() == {"changed": True, "msg": "No es primo"}  
