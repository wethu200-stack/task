def calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display operator options
    print("Choose an operator:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user operator choice
    choice = input("Enter the number of your chosen operator: ")
    
    # Perform operation
    if choice == '1':
        result = num1 + num2
        operator = '+'
    elif choice == '2':
        result = num1 - num2
        operator = '-'
    elif choice == '3':
        result = num1 * num2
        operator = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operator = '/'
        else:
            print("Error: Division by zero!")
            
            return
    else:
        print("Invalid operator choice!")
        return
    
    # Print result
    print(f"{num1} {operator} {num2} = {result}")

# Call the function
calculator()