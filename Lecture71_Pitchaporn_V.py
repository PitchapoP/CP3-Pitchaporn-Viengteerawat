menuList = []
priceList = []

def ShowBill():
  print(' My Food '.center(15, '-'))
  for number in range(len(menuList)):
    print(menuList[number], priceList[number])
  print(''.center(15, '-'))
  print('Totle price:', sum(priceList))

while True:
  menuName = input('Please Enter Menu : ')
  if (menuName.lower() == 'exit'):
    break
  else:
    menuPrice = int(input('Price : '))
    menuList.append(menuName)
    priceList.append(menuPrice)

ShowBill()