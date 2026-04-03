import os
import subprocess
import sys

def check_environment():
    print("Checking Python version...")
    assert sys.version_info >= (3, 8), "Python 3.8+ required"
    
    print("Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_database():
    print("Setting up database...")
    from app import app, db
    with app.app_context():
        db.create_all()
        print("Database tables created")

def configure_production():
    print("Configuring production settings...")
    
    os.environ['FLASK_ENV'] = 'production'
    os.environ['SECRET_KEY'] = os.urandom(24).hex()
    
    config = {
        'DEBUG': False,
        'TESTING': False,
        'SESSION_COOKIE_SECURE': True,
        'SESSION_COOKIE_HTTPONLY': True,
        'PERMANENT_SESSION_LIFETIME': 1800
    }
    
    return config

def run_tests():
    print("Running tests before deployment...")
    result = subprocess.run([sys.executable, "-m", "pytest", "test_app.py", "-v"])
    if result.returncode != 0:
        print("Tests failed! Deployment aborted.")
        sys.exit(1)
    print("All tests passed!")

def start_server():
    print("Starting production server...")
    print("Use gunicorn for production: gunicorn -w 4 -b 0.0.0.0:8000 app:app")
    
    subprocess.run([sys.executable, "app.py"])

if __name__ == "__main__":
    print("=== DEPLOYMENT SCRIPT ===")
    
    check_environment()
    run_tests()
    setup_database()
    
    print("\nDeployment preparation complete!")
    print("\nTo deploy on production server:")
    print("1. Set environment variables")
    print("2. Use gunicorn: gunicorn -w 4 -b 0.0.0.0:8000 app:app")
    print("3. Configure nginx as reverse proxy")
    print("4. Use PostgreSQL instead of SQLite for production")
    
    start_server()