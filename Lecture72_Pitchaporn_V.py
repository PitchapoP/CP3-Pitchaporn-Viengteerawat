menuList = []

def ShowBill():
  print(' My Food '.center(15, '-'))
  sum = 0
  for number in range(len(menuList)):
    print(menuList[number])
    sum += menuList[number][1]
  print(''.center(15, '-'))
  print('Totle price:', sum)

while True:
  menuName = input('Please Enter Menu : ')
  if (menuName.lower() == 'exit'):
    break
  else:
    menuPrice = int(input('Price : '))
    menuList.append([menuName, menuPrice])

ShowBill()