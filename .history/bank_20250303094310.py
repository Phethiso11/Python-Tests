bank_name = " Bank"  # You can change this to your preferred bank name
balance = 0.0
transaction_history = []

def check_balance():
    """Displays the current balance."""
    global balance
    print(f"Your current balance is: ${balance:.2f}")

def deposit_money():
    """Allows the user to deposit money."""
    global balance, transaction_history
    try:
        amount = float(input("Enter the amount to deposit: $"))
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposited ${amount:.2f}")
            print("Deposit successful.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def withdraw_money():
    """Allows the user to withdraw money."""
    global balance, transaction_history
    try:
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > 0:
            if balance >= amount:
                balance -= amount
                transaction_history.append(f"Withdrew ${amount:.2f}")
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def view_transaction_history():
    """Displays the transaction history."""
    if transaction_history:
        print("Transaction History:")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions yet.")

def main():
    """Main function to run the banking program."""
    global bank_name
    while True:
        print(f"\nWelcome to {bank_name}")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':
                check_balance()
            case '2':
                deposit_money()
            case '3':
                withdraw_money()
            case '4':
                view_transaction_history()
            case '5':
                print("Thank you for banking with us!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()