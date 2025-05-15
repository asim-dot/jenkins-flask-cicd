import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Jenkins CI/CD Demo' in response.data

def test_api_status(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'OK'

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About This App' in response.data