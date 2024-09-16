def main():
    num_years = int(input("Enter the number of years: "))
    
    
    total_rainfall = 0
    num_months = num_years * 12
    
    # Outer loop for each year
    for year in range(1, num_years + 1):
        print(f"Year {year}:")
        
        # Inner loop for each month
        for month in range(1, 13):
            # Ask the user for the rainfall in inches for the current month
            rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
            
            # Add the rainfall to the total
            total_rainfall += rainfall
    
    
    average_rainfall = total_rainfall / num_months
    
    # Display the results
    print(f"\nNumber of months: {num_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
