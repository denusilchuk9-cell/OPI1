import pytest
from app import app, db
from models import User, Post

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_registration(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123',
        'submit': True
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_login_logout(client):
    client.post('/register', data={
        'username': 'testuser2',
        'email': 'test2@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    })
    
    response = client.post('/login', data={
        'username': 'testuser2',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Welcome back' in response.data
    
    response = client.get('/logout', follow_redirects=True)
    assert b'logged out' in response.data

def test_protected_route(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert b'Please login first' in response.data

def test_create_post(client):
    client.post('/register', data={
        'username': 'postuser',
        'email': 'post@example.com',
        'password': 'pass123',
        'confirm_password': 'pass123'
    })
    client.post('/login', data={
        'username': 'postuser',
        'password': 'pass123'
    })
    
    response = client.post('/create_post', data={
        'title': 'Test Post',
        'content': 'This is a test post content'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Test Post' in response.data

def test_xss_prevention(client):
    client.post('/register', data={
        'username': 'xssuser',
        'email': 'xss@example.com',
        'password': 'pass123',
        'confirm_password': 'pass123'
    })
    client.post('/login', data={
        'username': 'xssuser',
        'password': 'pass123'
    })
    
    response = client.post('/create_post', data={
        'title': '<script>alert("xss")</script>',
        'content': 'Content'
    }, follow_redirects=True)
    
    assert b'<script>' not in response.data

if __name__ == '__main__':
    pytest.main(['-v'])