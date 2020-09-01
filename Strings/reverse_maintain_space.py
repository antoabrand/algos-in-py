# reverse a string while maintaing spacing of original string

test = 'Hello World! is a string test.'
reversed_string = test[::-1]
spaces = [] # track where spaces should be
answer = [] 

for i, character in enumerate(test):
  if character == ' ':
    answer.append(character)
  else:
    answer.append(None)

for i, character in enumerate(reversed_string): 
  if answer[i] == None:
    answer[i] = character
    
print(''.join(answer)) 