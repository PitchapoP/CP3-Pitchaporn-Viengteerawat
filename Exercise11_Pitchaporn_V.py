# userinput
number = int(input('Please put a number : '))

for x in range(number):
  print(' '*(range(number)[-1]-x), end='')
  print('*'*(x+1), end='')
  print('*'*x)