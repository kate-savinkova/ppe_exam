import csv

def readFile(filename):
  """Read a csv file and return the list of students

    Keyword arguments:
    filename -- csv file for reading  
  """
  students = []
  with open(filename, "r") as file:
    reader = csv.DictReader(file, delimiter = ',')
    for student in reader:
      students.append({'id': student['id'], 'name': student['name'], 'titleProject_id': student['titleProject_id'], 'class': student['class'], 'score': student['score']})
  return students

def findVladimir(students):
  """Output a line in the format 'Ты получил: <SCORE>, за проект - <PROJECT_NUM>'

    Keyword arguments:
    students -- List of dictionaries representing students
  """
  for student in students:
    if ((student['name'].split(' ')[0] == 'Хадаров') and (student['name'].split(' ')[1] == 'Владимир')):
      title = student['titleProject_id']
      score = student['score']
      print(f'Ты получил: {score}, за проект - {title}')

def findAverage(students):
  """Return the average value of students' scores

    Keyword arguments:
    students -- List of dictionaries representing students
  """
  col = 0
  sum = 0
  for student in students:
    if (student['score'] != 'None'):
      sum += int(student['score'])
      col += 1
  return round(sum / col, 3)

def writeFile(filename, students, average):
  """Open a csv file and write the modified data

    Keyword arguments:
    filename -- csv file for writing
    students -- List of dictionaries representing students
    average -- average value of students' scores
  """
  with open(filename, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["id","name","titleProject_id","class","score"])
    for student in students:
      if (student['score'] == 'None'):
        student['score'] = average
      file_writer.writerow([student['id'], student['name'], student['titleProject_id'], student['class'], student['score']])

# запускаем выполнение необходимых функций
students = readFile("student.csv")
findVladimir(students)
average = findAverage(students)
print(average)
writeFile("student_new.csv", students, average)
