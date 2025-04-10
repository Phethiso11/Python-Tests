
    # Initialize the fruits dictionary
    fruits = {
    "apple": "M3.5 per kg", 
    "banana": "M1.2 per kg",
    "cherry": "M5.0 per kg",
    "date": "M3.5 per kg",
    "elderberry": "M7.0 per kg",
    }

    while True:
        print("\nOptions:")
        print("1. Get the price of a fruit")
        print("2. Add a new fruit")
        print("3. Update the price of an existing fruit")
        print("4. Display all fruits and their prices")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Get the price of a fruit
            fruit_name = input("Enter the name of the fruit: ").strip()
            if fruit_name in fruits:
                print(f"The price of {fruit_name} is {fruits[fruit_name]} per kg.")
            else:
                print(f"{fruit_name} is not in the dictionary.")
        
        elif choice == "2":
            # Add a new fruit
            fruit_name = input("Enter the name of the fruit: ").strip()
            if fruit_name in fruits:
                print(f"{fruit_name} already exists in the dictionary.")
            else:
                
                    price = float(input(f"Enter the price of {fruit_name} per kg: "))
                    fruits[fruit_name] = price
                    print(f"{fruit_name} has been added with a price of {price} per kg.")
                
        
        elif choice == "3":
            # Update the price of an existing fruit
            fruit_name = input("Enter the name of the fruit: ").strip()
            if fruit_name in fruits:
                
                    price = float(input(f"Enter the new price of {fruit_name} per kg: "))
                    fruits[fruit_name] = price
                    print(f"The price of {fruit_name} has been updated to {price} per kg.")
                
            else:
                print(f"{fruit_name} is not in the dictionary.")
        
        elif choice == "4":
            # Display all fruits and their prices
            if fruits:
                print("\nFruits and their prices:")
                for fruit, price in fruits.items():
                    print(f"{fruit}: {price} per kg")
            else:
                print("The dictionary is empty.")
        
        elif choice == "5":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
