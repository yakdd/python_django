from django.shortcuts import render
from django.http import HttpResponse
import logging
from typing import Callable

logger = logging.getLogger(__name__)


def log_deco(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Загружена страница {func.__name__}')
        return result

    return wrapper


html_header = """
    <h1>Домашняя работа № 1</h1>
    <hr>
    <nav>
    <ul style="list-style: none; display: flex;">
        <li><a href="http://127.0.0.1:8000" style="padding: 10px;">главная</a></li>
        <li><a href="http://127.0.0.1:8000/about/" style="padding: 10px;">обо мне</a></li>
    </ul>
    </nav>
"""


@log_deco
def index(request):
    html_main = '''
    <h2>Главная страница</h2>
    <p>Первый опыт работы с Django. Пока интересно, но не все понятно. Надеюсь, дальше будет больше толка.</p>
    '''
    html = html_header + html_main
    return HttpResponse(html)


@log_deco
def about(request):
    html_about = """
    <h2>Обо мне</h2>
    <p>Студент GeekBrains курса "Веб разработка на Python".<br>
    Несколько ранее (~ 15 лет назад) имел небольшой опыт работы с PHP и JavaScrit</p>"""
    html = html_header + html_about
    return HttpResponse(html)
