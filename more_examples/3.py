import csv

with open('students_new.csv', encoding="utf8") as csvfile:
  reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
  data = sorted(reader, key=lambda x: x['titleProject_id'])

id_project = input()

while (id_project != 'СТОП'):
  id_project = int(id_project)
  for el in data:
    if int(el['titleProject_id']) == id_project:
      surname, name, patronymic = el["Name"].split()
      print(f"Проект №{id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el['score']}.")
      break
  else:
    print('Ничего не найдено')
  id_project = input()