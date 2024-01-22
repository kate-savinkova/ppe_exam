# Напишите программу, которая вычисляет значение арифметического выражения, записанного в постфиксной форме.
# В выражении используются только целые числа и знаки арифметических операций.
# Знак '/' обозначает целочисленное деление.

# Входные данные
# На вход программы подаётся символьная строка, которая содержит запись арифметического выражения в постфиксной форме.
# Элементы постфиксной записи разделены пробелами.

# Выходные данные
# Программа должна вывести значение переданного ей выражения. Если выражение записано неверно, программа должна
# вывести слово 'ERROR'.

def evaluate_postfix(expression):
  stack = []
  operators = set(['+', '-', '*', '/'])
  for token in expression.split():
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
      stack.append(int(token))
    elif (token in operators) and (len(stack) >= 2):
      operand2 = stack.pop()
      operand1 = stack.pop()

      if token == '+':
        stack.append(operand1 + operand2)
      elif token == '-':
        stack.append(operand1 - operand2)
      elif token == '*':
        stack.append(operand1 * operand2)
      elif token == '/':
        stack.append(operand1 // operand2)
    else:
      print("ERROR")
      break
  
  if (len(stack) == 1):
    return stack.pop()
  else:
    return None

expression = input("Введите арифметическое выражение в постфиксной форме: ")
result = evaluate_postfix(expression)

if (result != None):
  print("Результат:", result)
else:
  print("ERROR")