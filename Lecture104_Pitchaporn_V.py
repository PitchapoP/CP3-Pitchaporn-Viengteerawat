class Customer:
  name = ''
  lastName = ''
  age = 0

  def addCart(self):
    print('Added to Cart', self.name, self.lastName, "'s cart")

customer1 = Customer()
customer1.name = 'A'
customer1.lastName ='B'
customer1.addCart()

customer2 = Customer()
customer2.name = 'C'
customer2.lastName ='D'
customer2.addCart()

customer3 = Customer()
customer3.name = 'E'
customer3.lastName ='F'
customer3.addCart()

customer4 = Customer()
customer4.name = 'G'
customer4.lastName ='H'
customer4.addCart()