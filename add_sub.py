# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). 
#Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.

def input_num(number):
    return int(input(number))


def main():
    # Get user input for the two numbers
    num1 = input_num("Enter the first number (num1): ")
    num2 = input_num("Enter the second number (num2): ")

    addition = num1 + num2
    subtraction = num1 - num2

    # Print the results
    print(f"The sum of {num1} and {num2} is: {addition}")
    print(f"The difference when {num2} is subtracted from {num1} is: {subtraction}")

# Execute the main program
if __name__ == "__main__":
    main()
