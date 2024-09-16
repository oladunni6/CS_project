def calculate_points(books_purchased):
    if books_purchased == 0:
        return 0
    elif books_purchased == 2:
        return 5
    elif books_purchased == 4:
        return 15
    elif books_purchased == 6:
        return 30
    elif books_purchased >= 8:
        return 60
    else:
        return 0  # 
    
def main():
    # Ask the user for the number of books purchased
    books_purchased = int(input("Enter the number of books you have purchased this month: "))
    
    # Calculate the points based on the number of books purchased
    points_awarded = calculate_points(books_purchased)
    
    # Display the number of points awarded
    print(f"Number of points awarded: {points_awarded}")


if __name__ == "__main__":
    main()
