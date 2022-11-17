def vatCalculate():
  totalPrice = float(input('Total price: '))
  result = totalPrice + (totalPrice * (7/100))
  return result

print(vatCalculate())