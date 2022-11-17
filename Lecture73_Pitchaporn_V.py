menuDict = {'Kimbub': 40, 'Pizza': 109, 'Sandwich': 25}
menuList = []

def ShowBill():
  print(' My Food '.center(15, '-'))
  sum = 0
  for number in range(len(menuList)):
    print(menuList[number][0], menuList[number][1])
    sum += menuList[number][1]
  print(''.center(15, '-'))
  print('Totle price:', sum)

print(menuDict)
while True:
  menuName = input('Please Enter Menu : ')
  if (menuName.lower() == 'exit'):
    break
  else:
    menuList.append([menuName, menuDict[menuName]])

ShowBill()