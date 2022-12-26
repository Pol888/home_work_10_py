import json


def read_json():
    with open('database.json', 'r', encoding='utf-8') as file_file:
        file = json.load(file_file)
        return file


# Считывание и сохранение в базу данных
def write_json(file):
    print('saved')
    with open('database.json', 'w', encoding='utf-8') as file_file:
        json.dump(file, file_file)
        print('Сохранение завершено..')
