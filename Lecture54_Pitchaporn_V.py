def login():
  usernameInput = input('Username: ')
  passwordInput = input('Password: ')

  if (usernameInput == 'admin') and (passwordInput == '1234'):
    return True
  else:
    return False

def showMenu():
  print('---- iShop ----')
  print('1. Vat Calculator')
  print('2. Price Calculator')

def menuSelect():
  userSelected = int(input('>>'))
  return userSelected

def vatCalculate(totalPrice):
  vat = 7
  result = totalPrice + (totalPrice * (vat/100))
  return result

def priceCalculate():
  price1 = int(input('First Product Price : '))
  price2 = int(input('Second Product Price : '))
  return vatCalculate(price1+price2)

def program():
  if login() == True:
    print('Successfully login !')
    showMenu()
    select = menuSelect()
    if select==1:
      price = float(input('Price (THB) : '))
      print(vatCalculate(price))
    elif select==2:
      print(priceCalculate())
  else:
    print('Username or password is incorrect')
    program()

program()