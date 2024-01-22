import csv
import random

def generate_login(name, year):
    # Формирование логина на основе фамилии и года рождения
    last_name = name.split()[0]
    login = f"{last_name}_{year}"
    return login

def generate_password():
    # Генерация случайного пароля из 8 символов
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def process_visitors(input_file, output_file):
    # Чтение данных из входного файла
    with open(input_file, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        visitors = list(reader)

    # Добавление столбцов с логинами и паролями
    for visitor in visitors:
        if visitor['exhibition_passed'].lower() == 'true':
            year_of_birth = 2024 - int(visitor['age'])
            login = generate_login(visitor['name'], year_of_birth)
            password = generate_password()
            visitor['login'] = login
            visitor['password'] = password
        else:
            visitor['login'] = ''
            visitor['password'] = ''

    # Запись расширенных данных в выходной файл
    with open(output_file, "w", encoding='utf-8', newline='') as file:
        fieldnames = list(visitors[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(visitors)

# Пример использования
process_visitors("visitors.csv", "visitors_new.csv")
