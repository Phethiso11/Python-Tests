
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("\n")
            return "Error: Division by zero"
        return a / b

class Menu:
    def display_menu(self):
        print("\n")
        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

def main():
    calculator = Calculator()
    menu = Menu()
    
    while True:
        menu.display_menu()
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
                continue
            
            match choice:
                case '1':
                    print("\n")
                    print(f"Result: {calculator.add(num1, num2)}")
                case '2':
                    print(f"Result: {calculator.subtract(num1, num2)}")
                case '3':
                    print(f"Result: {calculator.multiply(num1, num2)}")
                case '4':
                    print(f"Result: {calculator.divide(num1, num2)}")
        else:
            print("\n")
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
