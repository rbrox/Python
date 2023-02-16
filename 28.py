#   Write a class called Product.
#   The class should have fields 
#   called name, amount, and price, holding the product’s name, 
#   the number of items of that product in stock, 
#   and the regular price of the product. 
#   There should be a method get_pricethat receives the number of items 
#   to be bought and returns a the cost of buying that many items, 
#   where the regular price is charged for orders of less than 10 items, 
#   a 10% discount is applied for orders of between 10 and 99 items, 
#   and a 20% discount is applied for orders of 100 or more items. 
#   There should also be a method called make_purchase
#   that receives the number of items to be bought and decreases amount by 
#   that much.

class Product:
    name = 'Product_name'
    amount = 0
    price = 0
    
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    
    def get_price(self, item):
        billed = item * self.price
        
        
        if item > 100:
            billed *= 0.8
        elif item >= 10:
            billed *= 0.9

        return billed
    
    def make_purachase(self, item):
        self.amount -= item
        return 'Purchase Sucess'


def main():
    
    potato = Product('potato', 100, 10)
    print(potato.get_price(10))
    print('Amount = ',potato.amount)
    potato.make_purachase(10)
    print('Amount = ',potato.amount)
    
    
main()