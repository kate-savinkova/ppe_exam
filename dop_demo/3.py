import csv

def searchVisitorInfo(ticket_number, filename):
    """
    Search for visitor information based on the ticket number.

    Args:
    ticket_number (int): The ticket number to search for.
    filename (str): The name of the CSV file for reading.

    Returns:
    None: The function prints the visitor information or a message if nothing is found.
    """
    with open(filename, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if int(row['ticket_number']) == ticket_number:
                visitor_name = row['name']
                age = row['age']
                exhibition_passed = row['exhibition_passed']
                status = 'прошел' if exhibition_passed.lower() == 'true' else 'не прошел'
                print(f"Билет №{ticket_number} принадлежит: {visitor_name}, возраст: {age} лет, он(а) {status} экскурсию.")
                return
    print("Билет не найден. Попробуйте другой номер.")

# Example usage:
filename = "visitors.csv"
while True:
    user_input = input("Введите номер билета (или СТОП для завершения): ")
    if user_input.upper() == 'СТОП':
        break
    try:
        ticket_number = int(user_input)
        searchVisitorInfo(ticket_number, filename)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число или СТОП.")
