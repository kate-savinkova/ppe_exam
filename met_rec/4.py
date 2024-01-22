import csv
import string
import random

def create_initials (s):
  names=s.split()
  return f'{names[0]}_{names[1][0]}{names[2][0]}'

def create_password():
  characters = string.ascii_letters + string.digits
  password = ''.join(random.choice(characters) for _ in range(8))
  return password

students_passwords=[]
with open('students.csv', encoding="utf8") as csvfile:
  reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
  for row in reader:
    row['login']=create_initials(row['Name'])
    row['password']=create_password()
    students_passwords.append(row)

with open('students_new.csv', 'w', newline='', encoding='utf-8') as file:
  w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
  w.writeheader()
  w.writerows(students_passwords)