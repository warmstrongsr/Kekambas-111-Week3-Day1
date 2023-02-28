# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []
        
    def add_to_cart(self, new_item):
        self.cart.append(new_item)
    #print
    def remove_from_cart(self):
        #self.cart - self.cart remove?pass
    
    def show_cart(self):
        pass
    
class Product:
    def __init__(self, name, quanity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def get_product_total(self):
        return self.quantity * self.price
    
    
def run():
    cust_name = input('Welcome. What is your name? ')
    my_cart = Cart(cust_name)
    
    
    while True:
        ask = input('What would you like to do? Add/Remove/Show/Quit ').lower()
        if ask == 'quit':
            break
        elif ask == 'add':#backwards I think (flip)
            item = input('What would you like to add? ')
            my_cart.add_to_cart(item)
            #remove
            #show?
            