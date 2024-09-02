def calculate_meal_total():
    
    food_charge = float(input("Enter the charge for the food: $"))

    
    tip_rate = 0.18
    tax_rate = 0.07

   
    tip_amount = food_charge * tip_rate
    tax_amount = food_charge * tax_rate

    
    total_price = food_charge + tip_amount + tax_amount

   
    print(f"Charge for the food: ${food_charge:.2f}")
    print(f"Tip amount (18%): ${tip_amount:.2f}")
    print(f"Sales tax amount (7%): ${tax_amount:.2f}")
    print(f"Total price: ${total_price:.2f}")


calculate_meal_total()
#calc
