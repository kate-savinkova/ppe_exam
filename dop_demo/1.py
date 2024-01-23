import csv

def readVisitors(filename):
  """Read a csv file and return the list of visitors and their information.

  Keyword arguments:
  filename -- csv file for reading
  """
  visitors = []
  with open(filename, "r", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for visitor in reader:
      # visitors.append({'ticket_number': int(visitor['ticket_number']), 'name': visitor['name'], 'exhibition_passed': visitor['exhibition_passed']})
      visitors.append(visitor)
  return visitors

def findIvan(visitor_data):
  """Output whether Ivan passed the exhibition based on ticket information.

  Keyword arguments:
  visitor_data -- List of dictionaries representing visitors and their ticket information
  """
  for visitor in visitor_data:
    if visitor['name'] == 'Иванов Иван Иванович':
      exhibition_passed = visitor['exhibition_passed']
      result = 'прошли' if exhibition_passed.lower() == 'true' else 'не прошли'
      print(f'Вы {result} экскурсию')

def calculatePercentages(visitor_data):
  """Return the percentages of visitors who passed and did not pass the exhibition.

  Keyword arguments:
  visitor_data -- List of dictionaries representing visitors and their ticket information
  """
  # total_visitors = 0
  # for visitor in visitor_data:
  #   if visitor['exhibition_passed'].lower() != 'none':
  #     total_visitors += 1
  total_visitors = sum(1 for visitor in visitor_data if visitor['exhibition_passed'].lower() != 'none')
  passed_visitors = sum(1 for visitor in visitor_data if visitor['exhibition_passed'].lower() == 'true')
  percentage_passed = (passed_visitors / total_visitors) * 100 if total_visitors > 0 else 0.0

  return percentage_passed

def correctData(visitor_data, percentage_passed):
  """Correct data based on the majority percentage.

  Keyword arguments:
  visitor_data -- List of dictionaries representing visitors and their ticket information
  percentage_passed -- Percentage of visitors who passed the exhibition
  percentage_not_passed -- Percentage of visitors who did not pass the exhibition
  """
  majority_passed = percentage_passed >= 50

  for visitor in visitor_data:
    if visitor['exhibition_passed'].lower() == 'none':
      visitor['exhibition_passed'] = 'true' if majority_passed else 'false'

def writeVisitors(filename, visitor_data):
  """Open a csv file and write the modified data.

  Keyword arguments:
  filename -- csv file for writing
  visitor_data -- List of dictionaries representing visitors and their ticket information
  """
  with open(filename, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",")
    file_writer.writerow(['ticket_number','name','age','exhibition_passed'])
    for visitor in visitor_data:
      file_writer.writerow([visitor['ticket_number'], visitor['name'], visitor['age'], visitor['exhibition_passed']])

# Run the necessary functions
filename = "visitors.csv"
visitors = readVisitors(filename)

# Find out if Ivan passed the exhibition
findIvan(visitors)

# Calculate percentages and correct data
percentage_passed = calculatePercentages(visitors)
correctData(visitors, percentage_passed)

# Write the corrected data to a new file
writeVisitors("visitors_new.csv", visitors)