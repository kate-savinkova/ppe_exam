import csv

def readVisitors(filename):
    """Read a csv file and return the list of visitors and their information.

    Keyword arguments:
    filename -- csv file for reading
    """
    visitors = []
    with open(filename, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for visitor in reader:
            visitors.append({'ticket_number': int(visitor['ticket_number']), 'name': visitor['name'], 'age': int(visitor['age']), 'exhibition_passed': visitor['exhibition_passed']})
    return visitors

def selectionSortByAge(visitors):
    """Sort visitors by age using selection sort.

    Keyword arguments:
    visitors -- List of dictionaries representing visitors and their information
    """
    n = len(visitors)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if visitors[j]['age'] < visitors[min_index]['age']:
                min_index = j
        visitors[i], visitors[min_index] = visitors[min_index], visitors[i]

def printTop3Youngest(visitors):
    """Print information about the top 3 visitors with the youngest age.

    Keyword arguments:
    visitors -- List of dictionaries representing visitors and their information
    """
    print("Топ-3 посетителей с наименьшим возрастом:")
    for i in range(min(3, len(visitors))):
        place = i + 1
        name = visitors[i]['name']
        print(f"{place} место: {name}")

# Пример использования:
filename = "visitors.csv"
visitors = readVisitors(filename)

# Сортировка по возрасту с использованием сортировки выбором
selectionSortByAge(visitors)

# Вывод топ-3 посетителей с наименьшим возрастом
printTop3Youngest(visitors)
