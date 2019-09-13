# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для игры
import random
from dialog import *

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
    # Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )


# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new'] or user_id not in sessionStorage:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его, показав правила игры
        fingers_prev = random.randint(0, 10)
        fingers_curr = random.randint(0, 10)

        sessionStorage[user_id] = {
            'fingers_prev': fingers_prev,
            'fingers_curr': fingers_curr,
            'count_fail': 0,
            'count_success': 0,
            'count_game': 0
        }

        if req['session']['new']:
            res['response']['text'] = 'Привет, давай сыграем!\n'
        else:
            res['response']['text'] = 'Решил сыграть ещё раз?\n'
        # Сохраняем данные о пальцах, добавляем правила
        sessionStorage[user_id]['fingers_prev'] = fingers_curr
        sessionStorage[user_id]['fingers_curr'] = first_question(res, fingers_prev, fingers_curr)

        return

    # Обрабатываем ответ пользователя.
    client_numb = -1
    client_count = 0
    for obj in req['request']['nlu']['entities']:
        if obj['type'] == 'YANDEX.NUMBER':
            client_numb = obj['value']
            client_count += 1

    if client_count == 1 and -1 < client_numb < 11:
        # Получаем данные из хранилища
        fingers_prev = sessionStorage[user_id]['fingers_prev']
        fingers_curr = sessionStorage[user_id]['fingers_curr']
        count_success = sessionStorage[user_id]['count_success']
        count_fail = sessionStorage[user_id]['count_fail']

        # Проверяем ответ клиента
        if client_numb == fingers_prev:
            res['response']['text'] = random.choice(true_answers)
            count_fail = 0
            count_success += 1
        else:
            res['response']['text'] = random.choice(wrong_answers) + ' это ' + str(
                fingers_prev) + ' ' + get_finger_word(fingers_prev) + '\n'
            count_fail += 1
            count_success = 0

        # Сохраняем счётчики
        sessionStorage[user_id]['count_fail'] = count_fail
        sessionStorage[user_id]['count_success'] = count_success
        # sessionStorage[user_id]['count_game'] += 1

        # Задаём новый вопрос
        if count_fail == 5:
            fingers_prev = random.randint(0, 10)
            fingers_curr = random.randint(0, 10)

            sessionStorage[user_id]['fingers_prev'] = fingers_curr
            sessionStorage[user_id]['fingers_curr'] = first_question(res, fingers_prev, fingers_curr)

            sessionStorage[user_id]['count_fail'] = 0
            return
        else:
            if count_success == 4:
                res['response']['text'] += 'Ого, кажется ты смог разобраться в этой игре! Прими мои поздравления!\n'
                sessionStorage.pop(user_id)
                return

            fingers_prev = fingers_curr
            fingers_curr = random.randint(0, 10)

            res['response']['text'] += random.choice(asks)
            if random.randint(0, 2) == 0:
                res['response']['text'] += random.choice(other_emoji)
            res['response']['text'] += get_fingers(fingers_curr)

            sessionStorage[user_id]['fingers_prev'] = fingers_prev
            sessionStorage[user_id]['fingers_curr'] = fingers_curr

        return

    # Если нет, просим ответить по другому
    res['response']['text'] = random.choice(not_valid_answers)
    if client_count > 1:
        res['response']['text'] += 'Пожалуйста выберите один ответ.\n'


# Демонстрирует правила
def first_question(res, fingers_prev, fingers_curr):
    fingers_next = random.randint(0, 10)
    res['response']['text'] += 'Смотри, это ' + get_fingers(fingers_prev) + ' - ' + str(
        fingers_prev) + ' ' + get_finger_word(fingers_prev) + '\n' + \
        'и это: ' + get_fingers(fingers_curr) + ' - ' + str(
        fingers_prev) + ' ' + get_finger_word(fingers_prev) + '\n' + \
        'А сколько это пальцев? ' + get_fingers(fingers_next)

    return fingers_next


def get_fingers(fingers):
    if fingers == 0:
        return random.choice(fingers_null)
    elif fingers == 1:
        return random.choice(fingers_one)
    elif fingers == 2:
        return random.choice(fingers_two)
    elif fingers == 3:
        return random.choice(fingers_three)
    elif fingers == 4:
        return random.choice(fingers_three) + random.choice(fingers_one)
    elif fingers == 5:
        return random.choice(fingers_five)
    elif fingers == 6:
        return random.choice(fingers_five) + random.choice(fingers_one)
    elif fingers == 7:
        return random.choice(fingers_five) + random.choice(fingers_two)
    elif fingers == 8:
        return random.choice(fingers_five) + random.choice(fingers_three)
    elif fingers == 9:
        return random.choice(fingers_five) + random.choice(fingers_three) + random.choice(fingers_one)
    elif fingers == 10:
        return random.choice(fingers_ten)
    return False


def get_finger_word(fingers):
    if fingers == 0 or fingers > 4:
        return 'пальцев'
    elif 1 < fingers < 5:
        return 'пальца'
    elif fingers == 1:
        return 'палец'

