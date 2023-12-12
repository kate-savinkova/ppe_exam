# реализация с помощью цикла
def is_correct_brackets_while(text):
  while '()' in text or '[]' in text or '{}' in text:
    text = text.replace('()', '')
    text = text.replace('[]', '')
    text = text.replace('{}', '')

  return not text


print("Реализация с помощью цикла:")

print(is_correct_brackets_while('(((())))'))  # True
print(is_correct_brackets_while('(((())'))  # False
print(is_correct_brackets_while('())))'))  # False
print(is_correct_brackets_while('((((){}[]{}[])))'))  # True
print(is_correct_brackets_while('(){}[]{}[])))'))  # False
print(is_correct_brackets_while('(){}[]{}[]'))  # True

def is_correct_brackets_stack(expr):
  stack = []
  for char in expr:
    if char in ["(", "{", "["]:
      stack.append(char)
    else:
      if not stack:
        return False
      current_char = stack.pop()
      if current_char == '(':
        if char != ")":
          return False
      if current_char == '{':
        if char != "}":
          return False
      if current_char == '[':
        if char != "]":
          return False
        
  if stack:
    return False
  return True

print("Реализация с помощью стека:")

print(is_correct_brackets_stack('(((())))'))  # True
print(is_correct_brackets_stack('(((())'))  # False
print(is_correct_brackets_stack('())))'))  # False
print(is_correct_brackets_stack('((((){}[]{}[])))'))  # True
print(is_correct_brackets_stack('(){}[]{}[])))'))  # False
print(is_correct_brackets_stack('(){}[]{}[]'))  # True
