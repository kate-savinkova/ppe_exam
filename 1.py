import csv
students = []
def findVladimir(students):
  """Outputs a line in the format 'Ты получил: <SCORE>, за проект - <PROJECT_NUM>'

    Keyword arguments:
    students -- list of students
  """
  for student in students:
    if ((student['name'].split(' ')[0] == 'Хадаров') and (student['name'].split(' ')[1] == 'Владимир')):
      title = student['titleProject_id']
      score = student['score']
      print(f'Ты получил: {score}, за проект - {title}')

def findAverage(students):
  """Returns the average value of students' scores

    Keyword arguments:
    students -- list of students
  """
  col = 0
  sum = 0
  for student in students:
    if (student['score'] != 'None'):
      sum += int(student['score'])
      col += 1
  return round(sum / col, 3)

# считываем строки файла и кладем их в список students
with open("./student.csv", "r") as file:
  reader = csv.DictReader(file, delimiter = ',')
  for student in reader:
    students.append({'id': student['id'], 'name': student['name'], 'titleProject_id': student['titleProject_id'], 'class': student['class'], 'score': student['score']})

# запускаем выполнение необходимых функций
findVladimir(students)
average = findAverage(students)

# открываем на запись файл student_new.csv и заполняем данными с найденным средним значением оценки студентов
with open("student_new.csv", mode="w", encoding='utf-8') as w_file:
  file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
  file_writer.writerow(["id","name","titleProject_id","class","score"])
  for student in students:
    if (student['score'] == 'None'):
      student['score'] = average
    file_writer.writerow([student['id'], student['name'], student['titleProject_id'], student['class'], student['score']])
