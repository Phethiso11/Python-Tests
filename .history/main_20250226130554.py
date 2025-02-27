def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        
        return "Error: Division by zero"
    return a / b

def display_menu():
    print("\n")
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1/2/3/4/5): ")
        
        if choice == '5':
            print("\n")
            print("Exiting the program.")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                print("\n")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("\n")
                print("Invalid input. Please enter numeric values.")
            except:
                continue
            
            match choice:
                case '1':
                    print("\n")
                    print(f"Result: {add(num1, num2)}")
                case '2':
                    print(f"Result: {subtract(num1, num2)}")
                case '3':
                    print(f"Result: {multiply(num1, num2)}")
                case '4':
                    print(f"Result: {divide(num1, num2)}")
        else:
            print("\n")
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()