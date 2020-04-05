def get_characters(num):
  
  if num == 2:
    return 'abc'
  elif num == 3:
    return 'def'
  elif num == 4:
    return 'ghi'
  elif num == 5:
    return 'jkl'
  elif num == 6:
    return 'mno'
  elif num == 7:
    return 'pqrs'
  elif num == 8:
    return 'tuv'
  elif num == 9:
    return 'wxyz'
  else:
    return ''
    
    
def keypad(num):
  
  if num <= 1:
    return ['']
  elif 1 < num <= 9:
    return list(get_characters(num))
    
  last_digit = num % 10
  rest_num = num // 10
  string = get_characters(last_digit)
  output = list()
  
  for char in string:
    for digit in rest_num:
      new_digit = digit + char
      output.append(new_digit)
  return output
  
if __name__ == '__main__':
  print(keypad(5))
  print(keypad(456))
  print(keypad(942))
  print(keypad(113))
