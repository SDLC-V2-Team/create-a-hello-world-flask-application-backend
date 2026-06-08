import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_returns_greeting(client):
    """Happy path: GET / should return 200 and 'Hello World'."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World'

def test_not_found(client):
    """Error path: GET on undefined route returns 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_method_not_allowed(client):
    """Error path: POST on the only GET route returns 405."""
    response = client.post('/')
    assert response.status_code == 405

def test_trailing_slash_redirect(client):
    """Edge case: trailing slash on GET / causes a redirect (308)."""
    response = client.get('/?')
    # Flask with strict_slashes=True redirects to the canonical URL (without slash)
    assert response.status_code == 308
    # Optionally check that Location header points to '/'
    assert response.location == 'http://localhost/'

def test_app_is_flask_instance():
    """Ensure the app object is a Flask instance."""
    from flask import Flask
    assert isinstance(app, Flask)