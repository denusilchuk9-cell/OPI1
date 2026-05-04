from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Вітаю! Блог працює!</h1>
        <p>Сторінки:</p>
        <ul>
            <li><a href="/admin/">Адмін-панель</a></li>
            <li><a href="/create/">Створити пост</a></li>
            <li><a href="/register/">Реєстрація</a></li>
            <li><a href="/login/">Вхід</a></li>
        </ul>
    """)

def post_detail(request, post_id):
    return HttpResponse(f"<h1>Пост #{post_id}</h1>")

def create_post(request):
    return HttpResponse("<h1>Створення нового поста</h1><p>Тут буде форма</p>")

def register(request):
    return HttpResponse("<h1>Реєстрація користувача</h1><p>Тут буде форма реєстрації</p>")

def user_login(request):
    return HttpResponse("<h1>Вхід в систему</h1><p>Тут буде форма входу</p>")

def user_logout(request):
    return HttpResponse("<h1>Вихід</h1><p>Ви вийшли з системи. <a href='/'>На головну</a></p>")