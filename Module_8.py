class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
       


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                if item.item_price != 0:
                    self.cart_items[i].item_price = item.item_price
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        total_cost = 0
        for item in self.cart_items:
            item.print_item_cost()
            total_cost += item.item_price * item.item_quantity
        print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description if (item, 'item_description') else 'No description'}")


def print_menu(cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    choice = input("Choose an option: ")
    return choice


def main():
    item1 = ItemToPurchase()
    item1.item_name = input("Item 1\nEnter the item name:\n")
    item1.item_price = (input("Enter the item price:\n"))
    item1.item_quantity = (input("Enter the item quantity:\n"))

    item2 = ItemToPurchase()
    item2.item_name = input("Item 2\nEnter the item name:\n")
    item2.item_price = (input("Enter the item price:\n"))
    item2.item_quantity = (input("Enter the item quantity:\n"))

    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print("\nTotal Cost")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost}")

    customer_name = input("\nEnter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    while True:
        choice = print_menu(cart)
        
        if choice == 'q':
            break
        elif choice == 'a':
            print("Add item to cart")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            item.item_description = item_description
            cart.add_item(item)
        elif choice == 'r':
            print("Remove item from cart")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c':
            print("Change quantity of Item")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name, quantity=new_quantity)
            cart.modify_item(item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
