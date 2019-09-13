import emoji

# Списки фраз для общения с игроком
asks = [
    'А сколько это пальцев?\n',
    'Сколько пальцев на этот раз?\n',
    'А сейчас?\n',
    'Сколько пальцев я показываю?\n'
]

true_answers = [
    'Правильно!\n',
    'Молодец!\n',
    'Угадал, попробуешь ещё?\n'
]

wrong_answers = [
    'Нет!\n',
    'Подумай еще...\n',
    'Не угадал.\n'
]

not_valid_answers = [
    'Пытаешься меня отвлечь?)\n',
    'Извините?\n',
    'Это не ответ.\n',
    'Может это и так.\n',
]

digit_answers = [
    'ноль', '0',
    'один', '1',
    'два', '2',
    'три', '3',
    'четыре', '4',
    'пять', '5',
    'шесть', '6',
    'семь', '7',
    'восемь', '8',
    'девять', '9',
    'десять', '10'
]

# Списки с различными эмоджи пальцев
fingers_null = [
    emoji.emojize(':raised_fist:'),
    emoji.emojize(':oncoming_fist:'),
    emoji.emojize(':left-facing_fist:'),
    emoji.emojize(':right-facing_fist:')
]

fingers_one = [
    emoji.emojize(':thumbs_down:'),
    emoji.emojize(':thumbs_up:'),
    emoji.emojize(':backhand_index_pointing_left:'),
    emoji.emojize(':backhand_index_pointing_right:'),
    emoji.emojize(':backhand_index_pointing_up:'),
    emoji.emojize(':backhand_index_pointing_down:'),
    emoji.emojize(':shushing_face:')
]

fingers_two = [
    emoji.emojize(':victory_hand:'),
    emoji.emojize(':crossed_fingers:'),
    emoji.emojize(':sign_of_the_horns:'),
    emoji.emojize(':call_me_hand:'),
    emoji.emojize(':thinking_face:')
]

fingers_three = [
    emoji.emojize(':love-you_gesture:'),
]

fingers_five = [
    emoji.emojize(':clapping_hands:'),
    emoji.emojize(':waving_hand:'),
    emoji.emojize(':raised_back_of_hand:'),
    emoji.emojize(':hand_with_fingers_splayed:'),
    emoji.emojize(':raised_hand:'),
    emoji.emojize(':vulcan_salute:'),
    emoji.emojize(':face_with_hand_over_mouth:')
]

fingers_ten = [
    emoji.emojize(':raising_hands:'),
    emoji.emojize(':open_hands:'),
    emoji.emojize(':palms_up_together:'),
    emoji.emojize(':hugging_face:'),
]

other_emoji = [
    emoji.emojize(':astonished_face:'),
    emoji.emojize(':grinning_face:'),
    emoji.emojize(':winking_face:'),
    emoji.emojize(':face_blowing_a_kiss:'),
    emoji.emojize(':winking_face_with_tongue:'),
    emoji.emojize(':zipper-mouth_face:'),
    emoji.emojize(':lying_face:'),
    emoji.emojize(':sleeping_face:'),
]

