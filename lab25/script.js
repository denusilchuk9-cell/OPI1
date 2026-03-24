const API_URL = 'http://localhost:5000/api';

async function checkConnection() {
    try {
        const response = await fetch('http://localhost:5000/health');
        if (response.ok) {
            const statusDiv = document.getElementById('status');
            statusDiv.textContent = '✅ Підключено до сервера';
            statusDiv.className = 'status online';
            return true;
        }
    } catch (error) {
        const statusDiv = document.getElementById('status');
        statusDiv.textContent = '❌ Немає з'єднання з сервером';
        statusDiv.className = 'status offline';
        return false;
    }
}

async function loadUsers() {
    try {
        const response = await fetch(`${API_URL}/users`);
        if (!response.ok) throw new Error('Помилка завантаження');
        
        const users = await response.json();
        const container = document.getElementById('usersContainer');
        
        if (users.length === 0) {
            container.innerHTML = '<div class="loading">Немає користувачів</div>';
            return;
        }
        
        container.innerHTML = users.map(user => `
            <div class="user-item">
                <div class="user-info">
                    <div class="user-name">${escapeHtml(user.name)}</div>
                    <div class="user-email">${escapeHtml(user.email)}</div>
                </div>
                <button class="delete-btn" onclick="deleteUser(${user.id})">🗑️ Видалити</button>
            </div>
        `).join('');
    } catch (error) {
        showError('Помилка завантаження користувачів');
    }
}

async function addUser() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    if (!name || !email) {
        showError('Будь ласка, заповніть всі поля');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/users`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error);
        }
        
        document.getElementById('name').value = '';
        document.getElementById('email').value = '';
        
        showSuccess('Користувача успішно додано!');
        
        await loadUsers();
    } catch (error) {
        showError(error.message);
    }
}

async function deleteUser(id) {
    if (!confirm('Ви впевнені, що хочете видалити цього користувача?')) return;
    
    try {
        const response = await fetch(`${API_URL}/users/${id}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error);
        }
        
        showSuccess('Користувача видалено!');
        await loadUsers();
    } catch (error) {
        showError(error.message);
    }
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 3000);
}

function showSuccess(message) {
    const successDiv = document.getElementById('success');
    successDiv.textContent = message;
    successDiv.style.display = 'block';
    setTimeout(() => {
        successDiv.style.display = 'none';
    }, 3000);
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

async function init() {
    await checkConnection();
    await loadUsers();
}

init();