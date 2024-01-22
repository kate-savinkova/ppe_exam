import csv

def generate_hash(s):
  alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
  d = {l: i for i, l in enumerate(alphabet,1)}
  p = 67
  m = 1e9 + 9
  hash_value = 0
  p_pow = 1
  for c in s:
    hash_value = (hash_value + d[c] * p_pow) % m
    p_pow = (p_pow * p) % m
  return int(hash_value)

students_with_hash=[]

with open('students.csv', encoding="utf8") as csvfile:
  reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
  for row in reader:
    row['id']=generate_hash(row['Name'])
    print(row)
    students_with_hash.append(row)

with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
  w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
  w.writeheader()
  w.writerows(students_with_hash)