# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_get_form(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'<textarea' in rv.data

def test_post_small_graph(client):
    data = "3 2\n1 3\n2 3\n"
    resp = client.post('/', data={'input_data': data})
    assert resp.status_code == 200
    text = resp.data.decode('utf-8')
    # проверяем, что во вёрстке появился правильный ответ
    assert "2" in text.splitlines()[text.splitlines().index("<h2>Результат:</h2>") + 1]
    assert "1" in text
    assert "3" in text
