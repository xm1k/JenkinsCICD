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
    lines = text.splitlines()
    # находим строку с <h2>Результат:</h2> и смотрим следующую за ней
    idx = lines.index("<h2>Результат:</h2>") + 1

    # проверяем, что в первой строке результата указано 3
    assert "3" in lines[idx]

    # проверяем, что в блоке <pre> есть все три вершины
    assert "1" in text
    assert "2" in text
    assert "3" in text
