from robots.models import Robot
from utils import *
import mimetypes
from django.http import HttpResponse


# Create your views here.
def report(request):
    # Выборка роботов, созданных за последнюю неделю
    robots_info = Robot.objects.raw("""select id, model, version , 
                                    count(version) as counter from robots_robot
                                    where created >= datetime('now', '-7 day')
                                    group by version""")
    # Составление словаря по моделям и версиям
    dict_for_report = dict()
    for i in robots_info:
        if i.model in dict_for_report.keys():
            dict_for_report[i.model].append(i)
        else:
            dict_for_report[i.model] = [i]
    rep = ReportCreator()
    # Создание Excel отчета
    path = rep.create_report(dict_for_report)
    excel_doc = open(path, 'rb')
    mime_type, _ = mimetypes.guess_type(path)
    # Формирование Http ответа с Excel отчетом
    response = HttpResponse(excel_doc, content_type=mime_type)
    excel_doc.close()
    return response
