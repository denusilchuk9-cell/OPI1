const request = require('supertest');
const app = require('../backend/server');

describe('Integration Tests', () => {
    
    describe('IP-1: API Endpoints', () => {
        
        test('GET /api/users - should return users list', async () => {
            const response = await request(app)
                .get('/api/users')
                .expect('Content-Type', /json/)
                .expect(200);
            
            expect(Array.isArray(response.body)).toBe(true);
            expect(response.body[0]).toHaveProperty('id');
            expect(response.body[0]).toHaveProperty('name');
            expect(response.body[0]).toHaveProperty('email');
        });
        
        test('POST /api/users - should create new user', async () => {
            const newUser = {
                name: 'Тестовий Користувач',
                email: 'test@example.com'
            };
            
            const response = await request(app)
                .post('/api/users')
                .send(newUser)
                .expect(200);
            
            expect(response.body).toHaveProperty('id');
            expect(response.body.name).toBe(newUser.name);
            expect(response.body.email).toBe(newUser.email);
        });
        
        test('POST /api/users - should return 400 for invalid data', async () => {
            const invalidUser = { name: 'Only Name' };
            
            const response = await request(app)
                .post('/api/users')
                .send(invalidUser)
                .expect(400);
            
            expect(response.body).toHaveProperty('error');
        });
        
        test('DELETE /api/users/:id - should delete user', async () => {
            const newUser = {
                name: 'Для Видалення',
                email: 'delete@example.com'
            };
            
            const createResponse = await request(app)
                .post('/api/users')
                .send(newUser);
            
            const userId = createResponse.body.id;
            
            const deleteResponse = await request(app)
                .delete(`/api/users/${userId}`)
                .expect(200);
            
            expect(deleteResponse.body).toHaveProperty('message');
        });
    });
    
    describe('IP-2: Database Integration', () => {
        
        test('Database should be accessible', async () => {
            const response = await request(app)
                .get('/api/users')
                .expect(200);
            
            expect(response.body).toBeDefined();
        });
    });
    
    describe('System Health', () => {
        
        test('GET /health - should return system status', async () => {
            const response = await request(app)
                .get('/health')
                .expect(200);
            
            expect(response.body.status).toBe('ok');
            expect(response.body).toHaveProperty('timestamp');
        });
    });
});