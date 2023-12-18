import csv
import random
import string

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

def generate_password(length):
  """Generate a random password with the current length
  
    Keyword arguments:
    length -- Length of password
  """
  characters = string.ascii_letters + string.digits
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def generate_login(student):
  """Generate login information from student's name

    Keyword arguments:
    student -- dictionary with the information about student
  """
  login = student['name'].split()[1] + '_' + student['name'].split()[0][0] + student['name'].split()[2][0]
  return login

def writeFile(filename, students):
  """Open a csv file and write the modified data

    Keyword arguments:
    filename -- csv file for writing
    students -- List of dictionaries representing students
  """
  with open(filename, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["id","name","titleProject_id","class","score","login","password"])
    for student in students:
      file_writer.writerow([student['id'], student['name'], student['titleProject_id'], student['class'], student['score'], generate_login(student), generate_password(8)])

students = readFile("student.csv")
writeFile("students_password.csv", students)