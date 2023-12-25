import csv

with open('students.csv', encoding="utf8") as csvfile:
  reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
  for i in range(len(reader)):
    j = i - 1
    key = reader[i]
    while float(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < float(key['score'] if key['score'] != 'None' else 0) and j >= 0:
      reader[j + 1] = reader[j]
      j -= 1
    reader[j + 1] = key

print('10 класс:')
count = 1

for el in reader:
  if '10' in el['class']:
    surname, name, patronymic = el["Name"].split()
    print(f'{count} место: {name[0]}. {surname}')
    count += 1
  if count == 4:
    break