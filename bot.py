from aiogram import Bot, Dispatcher, executor, types
import read_and_write_in_database
from keyboard import kb_client, kb_client1
from config import TOKEN
import exporting_data


file = read_and_write_in_database.read_json()
b = Bot(token=TOKEN)
dp = Dispatcher(bot=b)


@dp.message_handler(commands=['start'])
async def f(message: types.Message):
    await b.send_message(message.from_user.id, f'Привет, Имя', reply_markup=kb_client)


@dp.message_handler()
async def f1(message: types.Message):
    if message.text == '/Найти_работника':
        await b.send_message(message.from_user.id, 'По какому критерию осуществлять поиск?', reply_markup=kb_client1)
        await message.delete()
    elif message.text == '/id' or '/id' in message.text:
        if message.text == '/id':
            await message.answer('Введите ID в формате: /id 12345')
            await message.delete()
        else:
            for i in file:
                if i['id'] == int(message.text.split()[1]):
                    await message.answer(f'ID Сотрудника - {int(message.text.split()[1])}, Имя - {i["last_name"]},'
                                         f' Фамилия - {i["first_name"]},'
                                         f' Должность - {i["position"]}, Номер для связи'
                                         f' - {i["phone_number"]}, Заработная плата = '
                                         f'{i["salary"]}.')

    elif message.text == '/Имя_и_Фамилия' or '/ns' in message.text:
        if message.text == '/Имя_и_Фамилия':
            await message.answer('Введите Имя и Фамилию в формате: /ns name surname')
            await message.delete()
        else:
            for i in file:
                if message.text.split()[1].lower() == i["last_name"].lower() \
                        and message.text.split()[2].lower() == i["first_name"].lower():
                    await message.answer(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, '
                                         f'Фамилия - {i["first_name"]},'f' Должность - {i["position"]},'
                                         f' Номер для связи - {i["phone_number"]}, Заработная плата = {i["salary"]}.')

    elif message.text == '/Вернуться_в_предыдущее_меню':
        await b.send_message(message.from_user.id, 'Главное меню', reply_markup=kb_client)
        await message.delete()

    elif message.text == '/Сделать_выборку_сотрудников_по_должности' or '/vs' in message.text:
        if message.text == '/Сделать_выборку_сотрудников_по_должности':
            a = set()
            for i in file:
                a.add(i["position"])
            await message.answer(f'В базе имеются следующие наименования должностей...{a}')
            await message.answer('Введите в формате: /vs должность')
        else:
            for i in file:
                if i["position"].lower() == message.text.split()[1].lower():
                    await message.answer(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, '
                                         f'Фамилия - {i["first_name"]},'
                          f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, '
                                         f'Заработная плата = {i["salary"]}.'
                                         )

    elif message.text == '/Сделать_выборку_сотрудников_по_зарплате' or '/vz' in message.text:
        if message.text == '/Сделать_выборку_сотрудников_по_зарплате':
            await message.answer('Введите в формате: /vz От До')
        else:
            for i in file:
                if float(message.text.split()[1]) <= i["salary"] <= float(message.text.split()[2]):
                    await message.answer(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, '
                                         f'Фамилия - {i["first_name"]},'
                                         f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, '
                                         f'Заработная плата = {i["salary"]}.')

    elif message.text == '/Добавить_сотрудника' or '/ds' in message.text:
        if message.text == '/Добавить_сотрудника':
            await message.answer('Введите в формате: /ds имя фамилия должность телефон зарплата')
        elif len(message.text.split()) == 6:
            dict_employee = {"id": file[-1]['id'] + 1, "last_name": message.text.split()[1],
                             "first_name": message.text.split()[2], "position": message.text.split()[3],
                             "phone_number": message.text.split()[4], "salary": float(message.text.split()[5])}
            await message.answer(f'Новый сотрудник: {dict_employee}')
            file.append(dict_employee)

    elif message.text == '/Удалить_сотрудника' or '/rs' in message.text:
        if message.text == '/Удалить_сотрудника':
            await message.answer('Введите в формате: /rs id имя фамилия')
        else:
            ID = message.text.split()[1]
            name = message.text.split()[2]
            surname = message.text.split()[3]
            for num, i in enumerate(file):
                if name.lower() == i["last_name"].lower() and surname.lower() == i["first_name"].lower() \
                        and int(ID) == i['id']:
                    await message.answer(f'{num + 1}. Сотрудник найден\n сотрудник удален')
                    await message.answer(i)
                    del file[num]
            await message.answer('В связи с удалением сотрудника id некоторых сотрудников может измениться')
            for j in range(len(file)):
                file[j]['id'] = j + 1

    elif message.text == '/Обновить_данные_сотрудника' or '/us' in message.text:
        if message.text == '/Обновить_данные_сотрудника':
            await message.answer('Список колонок: last_name, first_name, position, phone_number, salary')
            await message.answer('Введите в формате: /us id имя фамилия колонка новое_значение')

        else:
            ID = message.text.split()[1]
            name = message.text.split()[2]
            surname = message.text.split()[3]
            for num, i in enumerate(file):
                if name.lower() == i["last_name"].lower() and surname.lower() == i["first_name"].lower() \
                        and int(ID) == i['id']:
                    await message.answer(f'Сотрудник найден')
                    await message.answer(i)
                    file[num][message.text.split()[4]] = message.text.split()[5]
                    await message.answer(f'Данные изменились')
                    await message.answer(file[num])

    elif message.text == '/Экспортировать_данные_в_формате_json':
        exporting_data.write_json2(file)
        with open('file_exporting.json', 'rb') as doc:
            await b.send_document(message.from_user.id, doc)

    elif message.text == '/Экспортировать_данные_в_формате_csv':
        exporting_data.write_csv2(file)
        with open('file_exporting.csv', 'rb') as doc2:
            await b.send_document(message.from_user.id, doc2)

    elif message.text == '/Закончить_работу_и_сохранить_изменения':
        read_and_write_in_database.write_json(file)


async def on_start(_):
    print('Я родился!')




