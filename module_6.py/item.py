class ItemToPurchase:
    def __init__(self, name="", item_price=0, quantity=0, description=""):
        self.name = name
        self.item_price = item_price
        self.quantity = quantity
        self.description = description

    def item_cost(self):
        return self.item_price * self.quantity

    def print_item_cost(self):
        total_cost = self.item_cost()
        print(f"{self.name} {self.quantity} @ ${self.item_price} = ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, name):
        for item in self.cart_items:
            if item.name == name:
                self.cart_items.remove(item)
                print(f"{name} removed")
                return
        print(f"{name} not found in cart.")

    def modify_item(self, name, quantity):
        for item in self.cart_items:
            if item.name == name:
                item.quantity = quantity
                print(f"Quantity for {name} changed to {quantity}.")
                return
        print(f"{name} not found in cart.")

    def cart_cost(self):
        return sum(item.item_cost() for item in self.cart_items)

    def print_total(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {sum(item.quantity for item in self.cart_items)}")
        if not self.cart_items:
            print("No Items in Cart")
        else:
            total_cost = 0
            for item in self.cart_items:
                item.print_item_cost()
                total_cost += item.item_cost()
            print(f"Total: ${total_cost:.2f}")


def print_menu(shopping_cart):
    options = {
        'a': "Add item to cart",
        'r': "Remove item from cart",
        'c': "Change item quantity",
        'i': "Output item description",
        'o': "Output shopping cart",
        'q': "Quit"
    }

    def add_item_to_cart():
        name = input('Enter the name: ')
        item_price = int(input('Enter the price: '))
        quantity = int(input('Enter the quantity: '))
        description = input('Enter the description: ')
        new_item = ItemToPurchase(name, item_price, quantity, description)
        shopping_cart.add_item(new_item)

    def remove_item_from_cart():
        name = input('Enter the name: ')
        shopping_cart.remove_item(name)

    def change_item_quantity():
        name = input('Enter the name of the item to modify: ')
        quantity = int(input('Enter the new quantity: '))
        shopping_cart.modify_item(name, quantity)

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
            change_item_quantity()
        elif choice == 'i':
            for item in shopping_cart.cart_items:
                print(f"{item.name}: {item.description}")
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            print("Quit")
            break
        else:
            print("Choice is not valid. Try again.")

def main():
    shopping_cart = ShoppingCart("John Doe", "February 1, 2020")
    
    # Adding some example items
    shopping_cart.add_item(ItemToPurchase("Nike Romaleos 2", 189, 2, "Weightlifting shoes"))
    shopping_cart.add_item(ItemToPurchase("Chocolate Chips", 3, 5, "For baking"))
    shopping_cart.add_item(ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Wireless headphones"))

    print_menu(shopping_cart)

if __name__ == "__main__":
    main()
