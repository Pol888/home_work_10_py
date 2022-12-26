import json
import csv


def write_json2(file):
    with open('file_exporting.json', 'w', encoding='utf-8') as file_file:
        json.dump(file, file_file)


def write_csv2(file):
    list_csv = []
    for i in file:
        list_csv.append([i['id'], i['last_name'], i['first_name'], i['position'], i['phone_number'], i['salary']])

    with open('file_exporting.csv', 'w', encoding='utf-8', newline='') as file_file:
        writer = csv.writer(file_file)
        writer.writerow(['id', 'last_name', 'first_name', 'position', 'phone_number', 'salary'])
        for row in list_csv:
            writer.writerow(row)
