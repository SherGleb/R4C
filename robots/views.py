from django.http import HttpResponse
import json
from robots.models import Robot
from utils import *


def index(request):
    return HttpResponse('Главная')


def create(request):
    if request.method == 'POST':
        # Выгрузка json-строки в словарь
        new_robot = json.loads(request.body)
        # Создание экземпляра класса RobotsValidator
        validator = RobotsValidator()
        # Валидация данных
        if not validator.is_valid(new_robot):
            return HttpResponse('Данные некорректны')
        # Добавление новой записи в бд
        robot = Robot(serial=new_robot['model']+'-'+new_robot['version'], model=new_robot['model'],
                      version=new_robot['version'], created=new_robot['created'])
        robot.save()
        return HttpResponse("Данные загружены успешно")
    return HttpResponse("Отправьте POST запрос для добавления данных в БД")