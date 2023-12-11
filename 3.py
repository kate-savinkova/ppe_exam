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

def findStudentByID(titleProject_id, students):
  """Find a student by projects's ID from the given list of students

    Keyword arguments:
    id -- The unique identifier of the student's project to be found
    students -- List of dictionaries representing students
  """
  flag = 0
  for student in students:
    if (int(student['titleProject_id']) == int(titleProject_id)):
      print('Проект №' + student['titleProject_id'] + ' делал: ' + student['name'].split()[1][0] + '.' + student['name'].split()[0] + ' он(а) получил(а) оценку - ' + student['score'] + '.')
      flag = 1
      break
  if (flag == 0):
    print('Ничего не найдено')

def SearchingForStudents(students):
  """Print the main info about student with a project's id, passing to the terminal, and stops when input is the word "СТОП"

  Keyword arguments:
  students -- List of dictionaries representing students
  """
  id = input()
  while (id != 'СТОП'):
    findStudentByID(id, students)
    id = input()

students = readFile("student.csv")
SearchingForStudents(students)