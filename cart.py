#burger
def add_burger(key):
    if key in menu['burger']:
        if key in shopping_cart:
            shopping_cart[key]['quantity'] += 1
        else:
            shopping_cart[key] = {'quantity': 1, 'price': menu['burger'][key]}
    else:
        print('Sorry, that item is not on the menu.') 
#extras
def add_extras(extra):
    for key in extra:
        if key in menu['extras']:
            if key in shopping_cart:
                shopping_cart[key]['quantity'] += 1
            else:
                shopping_cart[key] = {'quantity': 1, 'price': menu['extras'][key]}
        else:
            print(f"Sorry, {key} is not an extra on the menu.")
def add_fries(key):
    if key in menu['fries']:
        if key in shopping_cart:
            shopping_cart[key]['quantity'] += 1
        else:
            shopping_cart[key] = {'quantity': 1, 'price': menu['fries'][key]}
    else:
        print('Sorry, that item is not on the menu.')

def add_rings(key):
    if key in menu['rings']:
        if key in shopping_cart:
            shopping_cart[key]['quantity'] += 1
        else:
            shopping_cart[key] = {'quantity': 1, 'price': menu['rings'][key]}
    else:
        print('Sorry, that item is not on the menu.')
def add_drink(key):
    if key in menu['drink']:
        if key in shopping_cart:
            shopping_cart[key]['quantity'] += 1
        else:
            shopping_cart[key] = {'quantity': 1, 'price': menu['drink'][key]}
    else:
        print('Sorry, that item is not on the menu.')
def remove_item_from_cart(item):
    if item not in shopping_cart:
        print(f"{item} not in cart!")
    else:
        if shopping_cart[item]['quantity'] == 1:
            del shopping_cart[item]
            print(f"{item} removed from cart!")
        else:
            shopping_cart[item]['quantity'] -= 1
            print(f"{item} x1 removed!")
        print_total()
# for item, quantity in shopping_cart.items():
#     print(f"{item} x{quantity}")
def view_cart():
    if not shopping_cart:
        print('Your cart is empty.')
    else:
        for item, values in shopping_cart.items():
            print(f"{item} {values}")
def clear_cart():
    shopping_cart.clear()
def print_total():
    total = 0
    for item, info in shopping_cart.items():
        item_price = info['price']
        item_quantity = info['quantity']
        item_total = item_price * item_quantity
        total += item_total 
        print(f"{item} x {item_quantity} @ ${item_price:.2f} each = ${item_total:.2f}")
    print(f"Total: ${total:.2f}")
    
menu = {          #menu dict -> 'key': {dict} -> {key:value pairs}
    # for size, price in burger
    'burger': {'double': 6.49, 'single': 4.99, 'junior': 3.99, 'kids': 2.49},
    # for extra, price in extras
    'extras': {'cheese': .99, 'bacon': 1.49, 'grilled-mushrooms': .99, 'sauteed-onions': .29},
    # for size, price in fries
    'fries': {'super-fry': 4.99, 'large-fry': 3.99, 'medium-fry': 2.99, 'small-fry': 1.99, 'kids-fry': .99},
    # for size, price in rings
    'rings': {'super-rings': 4.99, 'large-rings': 3.99, 'medium-rings': 2.99, 'small-rings': 1.99, 'kids': .99},
    # for size, price in drink
    'drink': {'super-drink': 1.99, 'large-drink': 1.49, 'medium-drink': .99, 'small-drink': .49, 'kids-drink': .49},
}
shopping_cart = {}
def run():
    while True:
        print("\nOptions:")
        print("[1] + [Enter]: Add items to current order.")
        print("[2] + [Enter]: View current order.")
        print("[3] + [Enter]: Remove item/s from the current order.")
        print("[4] + [Enter]: Checkout with current order.")
        print("[5] + [Enter]: Clear current order.")
        print("[Q] + [Enter]: Quit")
        user_action = input("Please enter the number associated with how you would like to proceed [1-6]: ").lower()
        print(f"Options:")
        if user_action == '1' or user_action == 'add':
#             print(menu)
            for key in menu:
                print(key.title() +'-')
#                 for size, price in menu[key].items():
#                     print(f"{size.title()}: ${price:.2f}")
            add_what = input("\nWhat would you like to add to this order?")
            add_what = str(add_what.lower())
            if add_what == "burger":
                print(menu['burger'])
                burger_size = input(f"What size burger would you like?")
                add_burger(burger_size)             
                
                for extra, price in menu['burger'].items():
                    extras = input("Would you like to add extra toppings to the burger? y/n")
                    if extras == "y":
                        print("Here are the available extras for your burger:")  
                        #print statement with available extras and price (for loop)
                        for extra, price in menu['extras'].items():
                            print(f"{extra} - ${price:.2f}")
                        chosen_extras = input(
                            "Please enter the extra you would like to add.")
                        chosen_extras = chosen_extras.split(",")
                        add_extras(chosen_extras)
                    else:
                        break    
            if add_what == "fries":
                print(menu['fries'])
                fry_size = input(f"What size fries would you like?")
                add_fries(fry_size)
            if add_what == "rings":
                print(menu['rings'])
                rings_size = input(f"What size onion rings would you like?")
                add_rings(rings_size)
            if add_what == "drink":
                print(menu['drink'])
                drink_size = input(f"What size drink would you like?")
                add_drink(drink_size)
            print(shopping_cart)
        elif user_action == "2" or user_action == "cart" or user_action == "view":
            print_total()
        elif user_action == "3" or user_action == "remove":
            remove_what = input("What would you like to remove?")
            remove_item_from_cart(remove_what)
        elif user_action == "4" or user_action == "checkout":
            print_total()
            clear_cart()
        elif user_action == "5" or user_action == "clear":
            clear_cart()
            print("The shopping cart is now cleared!")
        elif user_action.lower() == "q" or user_action == "":
            clear_cart()
            break
        else:
            print("Invalid option. Please try again.")
run()
# print(shopping_cart)
print_total()    