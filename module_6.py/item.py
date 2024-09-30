class ItemToPurchase:
    def __init__(self, name="", item_price=0, quantity=0, description=""):
        self.name = name
        self.item_price = item_price
        self.quantity = quantity
        self.description = description

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        
    def remove_item(self, name):
        for item in self.cart_items:
            if item.name == name:
                self.cart_items.remove(item)
                print(f"{name} removed")

    def items_costs(self):
        total_cost = self.item_price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.item_price} = ${total_cost}")


    def modify_item(self, ItemToPurchase):
        print("Not modified")

    def cart_cost(self):
        return sum(item.item_price * item.quantity for item in self.cart_items)

    def print_total(self):
        print("\nTotal in cart")
        if not self.cart_items:
            print("No Items in Cart")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {sum(item.quantity for item in self.cart_items)}")
            total_cost = 0
            for item in self.cart_items:
                total_cost += item.item_price * item.quantity
                item.items_costs()
            print(f"Total: ${total_cost}")

def print_menu(shoppingCart):
    options = {
        'a': "Add item into cart",
        'r': "Remove item from cart",
        'c': "Change item quantity",
        'i': "Item output' description",
        'o': "Output shopping cart",
        'q': "Quit"
    }

    def add_item_to_cart():
        name = input('Enter the name: ')
        item_price = int(input('Enter the price: '))
        quantity = int(input('Enter the quantity: '))
        description = input('Enter the description: ')
        new_item = ItemToPurchase(name, item_price, quantity, description)
        shoppingCart.add_item(new_item)

    def remove_item_from_cart():
        name = input('Enter the name:')
        shoppingCart.remove_item(name)

    while True:
        print("\nMENU")
        for key, value in options.items():
            print(f"{key} - {value}")
        choice = input("Choose an option: ")
        
        if choice == 'a':
            add_item_to_cart()
        elif choice == 'r':
            remove_item_from_cart()
        elif choice == 'c':
            print("Changed.")
        elif choice == 'i':
            shoppingCart.print_thedescriptions()
        elif choice == 'o':
            shoppingCart.print_total()
        elif choice == 'q':
            print("Quit")
            break
        else:
            print("Choice is not valid. Try again.")

def main():
    shopping_cart = ShoppingCart("", "February 1, 2020")
    print_menu(shopping_cart)

if __name__ == "__main__":
    main()