# Звіт: Системна інтеграція

## 1. Інтеграційні точки
- **IP-1:** Frontend (HTML/JS) ↔ Backend (Express) - REST API
- **IP-2:** Backend (Express) ↔ SQLite - SQL запити

## 2. Тестові випадки

| Тест | Дія | Очікуваний результат |
|------|-----|---------------------|
| TC-1 | GET /api/users | Код 200, список користувачів |
| TC-2 | POST /api/users | Код 200, створення користувача |
| TC-3 | DELETE /api/users/:id | Код 200, видалення |

## 3. Інструменти
- **Backend:** Node.js + Express
- **Database:** SQLite
- **Testing:** Jest + Supertest
- **CI/CD:** GitLab CI

## 4. Результати тестування
✓ GET /api/users - passed
✓ POST /api/users - passed
✓ DELETE /api/users/:id - passed
✓ Database connection - passed
✓ Health check - passed

Tests: 5 passed, 5 total

text

## 5. Виявлені проблеми
- **CORS помилка** → вирішено додаванням cors middleware
- **Дублікат email** → вирішено UNIQUE constraint в БД

## 6. Моніторинг
- Health check: `GET /health` → `{ status: "ok" }`
- Логування помилок в консоль

## 7. Висновок
✅ Всі інтеграційні точки працюють  
✅ Тести проходять (100%)  
✅ Система стабільна

---

## Як запустити
```bash
cd backend
npm install
node server.js
# Відкрити frontend/index.html в браузері
