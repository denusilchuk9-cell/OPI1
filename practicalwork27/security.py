import bcrypt
import re
from html import escape

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(hashed, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def validate_input(data):
    if data is None:
        return ''
    
    data = str(data).strip()
    data = escape(data)
    
    dangerous_patterns = [
        r'<script',
        r'javascript:',
        r'onclick',
        r'onload',
        r'onerror',
        r'<iframe',
        r'<object',
        r'<embed'
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, data, re.IGNORECASE):
            return ''
    
    return data

def sanitize_sql_input(value):
    dangerous_sql = [
        'DROP TABLE',
        'DELETE FROM',
        'TRUNCATE',
        'INSERT INTO',
        'UPDATE SET',
        'UNION SELECT',
        '--',
        ';'
    ]
    
    value_upper = value.upper()
    for sql in dangerous_sql:
        if sql in value_upper:
            return ''
    
    return value

def generate_csrf_token():
    import secrets
    return secrets.token_urlsafe(32)

def validate_email_domain(email):
    allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']
    if '@' in email:
        domain = email.split('@')[1]
        return domain in allowed_domains or len(allowed_domains) == 0
    return False