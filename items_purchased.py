class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


def get_item_info(item_number):
    print(f"Item {item_number}")
    item_name = input("Enter the item name:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    return ItemToPurchase(item_name, item_price, item_quantity)

item1 = get_item_info(1)
item2 = get_item_info(2)


print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()


total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

print(f"Total: ${total_cost}")