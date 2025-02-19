number = int(input("Please enter a number: "))

if number == 0:
    print("The number is zero.")

elif number > 0 and number % 2 == 0:
    print("The number is even and positive.")

elif number < 0 and number % 2 != 0:
    print("The number is odd and negative.")

elif number % 2 != 0:
    print("The number is odd.")

elif number % 2 == 0:
    print("The number is even.")

else:
    print("The number does not meet any specific condition.")
