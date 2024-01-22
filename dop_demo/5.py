import csv

# Функция для расчета хеша по алгоритму Multiplicative Hashing
def multiplicative_hash(full_name, A, m):
    hash_value = 0
    for char in full_name:
        hash_value = (hash_value * A + ord(char) - ord('a') + 1) % m
    return hash_value

# Функция для замены идентификаторов на хеши в CSV файле
def replace_ids_with_hashes(input_file_path, output_file_path, A, m):
    with open(input_file_path, 'r', newline='', encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames + ['hash']
        
        with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                row['hash'] = multiplicative_hash(row['name'], A, m)
                writer.writerow(row)

                # For testing purposes, let's also print the row to ensure it's being written correctly
                print(row)  
    print(f"Хеширование завершено. Результат сохранен в файл: {output_file_path}")


# Чтение данных из CSV файла и замена идентификаторов на хеши
input_file_path = 'visitors.csv'
output_file_path = 'visitors_new.csv'
A = 31  # выбранный коэффициент умножения
m = 118  # размер хеш-таблицы

replace_ids_with_hashes(input_file_path, output_file_path, A, m)

