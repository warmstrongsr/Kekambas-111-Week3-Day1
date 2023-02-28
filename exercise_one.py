# Create a class called cart that retains items and has methods to add, remove, and show

class Cart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []
        
    def add_to_cart(self, new_item):
        self.cart.append(new_item)
        print(f"{new_item.name} added to cart.")
    
    def remove_from_cart(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                print(f"{item.name} removed!")
                return
        print(f"{item_name} is not in your cart.")
    
    def show_cart(self):
        print(f"{self.customer_name}'s cart:")
        total_price = 0
        for item in self.cart:
            print(f"{item.name} - {item.quantity} - ${item.price}")
            total_price += item.price * item.quantity
        print(f"Total Price: ${total_price}")
    
class Product:
    def __init__(self, name, quantity, price):
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
        
        if ask == 'add':
            item_name = input('What would you like to add? ')
            item_quantity = int(input('How many would you like to add? '))
            item_price = float(input('What is the price per item? $'))
            new_item = Product(item_name, item_quantity, item_price)
            my_cart.add_to_cart(new_item)
            
        elif ask == 'remove':
            item_name = input('What would you like to remove? ')
            my_cart.remove_from_cart(item_name)
            
        elif ask == 'show':
            my_cart.show_cart()
            
        elif ask == 'quit':
            print('Thank you . Come again!')
            break
            
        else:
            print('Invalid action. Please try again.')
            
run()