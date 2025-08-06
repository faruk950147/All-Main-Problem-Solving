def menuDagon(num1, num2):
    while True:
        try:
            print("1. Add".center(10))
            print("2. Sub".center(10))
            print("3. Mul".center(10))
            print("4. Div".center(10))
            print("5. Exit".center(10))
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Addition".center(10))
                print("The Addition Result: ", num1 + num2)
            elif choice == 2:
                print("Subtraction".center(10))
                print("The Subtraction Result: ", num1 - num2)
            elif choice == 3:
                print("Multiplication".center(10))
                print("The Multiplication Result: ", num1 * num2)
            elif choice == 4:
                print("Division".center(10))
                print("The Division Result: ", num1 / num2)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
menuDagon(10, 20)
