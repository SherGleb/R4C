import re


class RobotsValidator:
    # Шаблон для проверки даты
    template = r"\d{1,}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    # Поля таблицы robot БД
    fields = ["model", "version", "created"]

    # Валидация json-строки из POST запроса
    @classmethod
    def is_valid(cls, dictionary):
        for i in cls.fields:
            if i not in dictionary.keys():
                return False
        if len(dictionary["model"]) != 2 or len(dictionary["version"]) != 2:
            return False
        if not re.fullmatch(cls.template, dictionary["created"]):
            return False
        return True