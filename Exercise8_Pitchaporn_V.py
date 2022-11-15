usernameInput = input('Username: ')
passwordInput = input('Password: ')

if (usernameInput == 'admin') and (passwordInput == '1234'):
  print('Successfully login !')
  print('---- iShop ----')
  basket = []
  while True:
    print('Welcome to iShop! Please select products you want to buy below')
    print('1. Banana  13 THB')
    print('2. Orange  8  THB')
    print('3. Apple   16 THB')
    print('4. Grape   24 THB')
    print(f'Total price: {sum(basket)}')
    print('please select 0 to stop the program')
    userSelected = int(input('>>'))
    if userSelected == 1:
      numberB = int(input('How many: '))
      priceB = 13
      basket.append(numberB*priceB)
      print('Added!', numberB*priceB, 'THB')
      print('--------------------')
    elif userSelected == 2:
      numberO = int(input('How many: '))
      priceO = 8
      basket.append(numberO*priceO)
      print('Added!', numberO*priceO, 'THB')
      print('--------------------')
    elif userSelected == 3:
      numberA = int(input('How many: '))
      priceA = 16
      basket.append(numberA*priceA)
      print('Added!', numberA*priceA, 'THB')
      print('--------------------')
    elif userSelected == 4:
      numberG = int(input('How many: '))
      priceG = 24
      basket.append(numberG*priceG)
      print('Added!', numberG*priceG, 'THB')
      print('--------------------')
    elif userSelected == 0:
      print('---- Thank you! ----\nTotal price are', sum(basket), 'THB')
      print('--------------------')
      break
    else:
      print('Input is invalid! please select again')
      print('--------------------')
else:
  print('Username or password is incorrect')