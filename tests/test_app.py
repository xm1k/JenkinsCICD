import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_endpoint_returns_reversed(client):
    resp = client.post('/process', json={'input': 'abc'})
    assert resp.status_code == 200
    assert resp.get_json() == {'output': 'cba'}
