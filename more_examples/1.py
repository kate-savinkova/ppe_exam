import csv

with open('students.csv', encoding="utf8") as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  answer = list(reader)[1:]
  for id, name, titleProject_id, level, score in answer:
    if 'Хадаров Владимир' in name:
      print(f"Ты получил: {score}, за проект - {titleProject_id}")
      break
  count_class = {}
  sum_class = {}
  for el in answer:
    count_class[el[-2]] = count_class.get(el[-2], 0) + 1
    sum_class[el[-2]] = count_class.get(el[-2], 0) + (int(el[-1]) if el[-1] != 'None' else 0)
  for el in answer:
    if el[-1] == 'None':
      el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open('students_new.csv', 'w', newline='', encoding='utf-8') as file:
  w = csv.writer(file)
  w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
  w.writerows(answer)