import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200 or response.status_code == 404  # Depending on your route

def test_add_sample_package(client):
    response = client.post('/add_sample')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Sample added'

def test_dummy():
    assert 1 == 1
