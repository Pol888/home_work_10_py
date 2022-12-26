from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('/Найти_работника')
b2 = KeyboardButton('/Сделать_выборку_сотрудников_по_должности')
b3 = KeyboardButton('/Сделать_выборку_сотрудников_по_зарплате')
b4 = KeyboardButton('/Добавить_сотрудника')
b5 = KeyboardButton('/Удалить_сотрудника')
b6 = KeyboardButton('/Обновить_данные_сотрудника')
b7 = KeyboardButton('/Экспортировать_данные_в_формате_json')
b8 = KeyboardButton('/Экспортировать_данные_в_формате_csv')
b9 = KeyboardButton('/Закончить_работу_и_сохранить_изменения')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8).add(b9)


b10 = KeyboardButton('/id')
b11 = KeyboardButton('/Имя_и_Фамилия')
b12 = KeyboardButton('/Вернуться_в_предыдущее_меню')
kb_client1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client1.add(b10, b11).add(b12)


b0 = KeyboardButton('/start')
kb_client0 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client0.add(b0)