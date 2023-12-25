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

def replace_null(list):
  """Replace the None field with 0

    Keyword arguments:
    list -- List of dictionaries representing students
  """
  for student in list:
    if (student['score'] == 'None'): student['score'] = 0

def insertion_sort(list, col):
  """Sort the list using the insertion sorting method

    Keyword arguments:
    list -- List of dictionaries representing students
    col -- Column by which the rows will be compared
  """
  for i in range(1, len(list)):
    temp = list[i]
    j = i - 1
    while (j >= 0 and int(temp[col]) < int(list[j][col])):
      list[j + 1] = list[j]
      j = j - 1
    list[j + 1] = temp

def output(list):
  """Output the first three students who received the highest score

    Keyword arguments:
    list -- List of dictionaries representing students
  """
  print("10 класс:")
  print("1 место: " + list[len(list) - 1]['name'].split(' ')[1][0] + '.' + list[len(list) - 1]['name'].split(' ')[0])
  print("2 место: " + list[len(list) - 2]['name'].split(' ')[1][0] + '.' + list[len(list) - 2]['name'].split(' ')[0])
  print("3 место: " + list[len(list) - 3]['name'].split(' ')[1][0] + '.' + list[len(list) - 3]['name'].split(' ')[0])

students = readFile("students.csv")
replace_null(students)
insertion_sort(students, 'score')
output(students)