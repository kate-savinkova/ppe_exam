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

def generate_hash(s):
  """Generate hash for string s

    Keyword arguments:
    s -- string for which the hash will be generated 
  """
  alphabet = [chr(i) for i in range(1040, 1104)]
  alphabet.append(' ')
  d = {l: i for i, l in enumerate(alphabet,1)}
  p = 67
  m = pow(10, 9) + 9
  hash_value = 0
  p_pow = 1
  for c in s:
    hash_value = (hash_value + d[c] * p_pow) % m
    p_pow = (p_pow * p) % m
  return int(hash_value)

def writeFile(filename, students):
  """Open a csv file and write the modified data

    Keyword arguments:
    filename -- csv file for writing
    students -- List of dictionaries representing students
  """
  with open(filename, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",")
    file_writer.writerow(["id","name","titleProject_id","class","score"])
    for student in students:
      student['id'] = generate_hash(student['name'])
      file_writer.writerow([student['id'], student['name'], student['titleProject_id'], student['class'], student['score']])

students = readFile("students.csv")
writeFile("students_with_hash.csv", students)