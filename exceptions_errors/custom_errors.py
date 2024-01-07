# we can raise custom errors with "raise" keyword
user_input = input("Enter a number between 5 and 9 or type 'quit' to exit: ")

try:
    if user_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
    else:
        number = int(user_input)
        if not (5 <= number <= 9):
            raise ValueError("Number is not in the specified range (5-9). Please try again.")
        
        print(f"You entered a valid number: {number}")

except ValueError as e:
    print(f"Error: {e}. Please enter a valid number or type 'quit' to exit.")

