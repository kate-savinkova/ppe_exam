import math

def evaluate_expression(expression):
  operators = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': (lambda x, y: x * y), '/': (lambda x, y: x / y)}

  stack = []
  tokens = expression.split()

  for token in tokens:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
      # Если токен - число, добавляем его в стек
      stack.append(float(token))
    elif token in operators:
      # Если токен - оператор, выполняем соответствующую операцию
      if len(stack) < 2:
        return 'ERROR'
      operand2 = stack.pop()
      operand1 = stack.pop()
      result = operators[token](operand1, operand2)
      stack.append(result)
    elif token.startswith('sin(') and token.endswith(')'):
      # Если токен - sin функция, вычисляем sin
      argument = float(token[4:-1])
      result = math.sin(argument)
      stack.append(result)
    elif token.startswith('cos(') and token.endswith(')'):
      # Если токен - cos функция, вычисляем cos
      argument = float(token[4:-1])
      result = math.cos(argument)
      stack.append(result)
    elif token.startswith('abs(') and token.endswith(')'):
      # Если токен - abs функция, вычисляем abs
      argument = float(token[4:-1])
      result = abs(argument)
      stack.append(result)
    elif token.startswith('sqrt(') and token.endswith(')'):
      # Если токен - sqrt функция, вычисляем sqrt
      argument = float(token[5:-1])
      result = math.sqrt(argument)
      stack.append(result)
    else:
      return 'ERROR'

  if len(stack) != 1:
    return 'ERROR'

  # Форматируем результат с тремя знаками после запятой
  formatted_result = format(stack[0], '.3f')
  return formatted_result

expression = input("Введите арифметическое выражение: ")
result = evaluate_expression(expression)
print("Результат:", result)
