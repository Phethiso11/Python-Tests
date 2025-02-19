number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

operation = input("Enter operation:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n: ")

if operation == '1':
	print("Result: ", int(number1) + int(number2))

elif operation == '2':
	print("Result: ", int(number1) - int(number2))

elif operation == '3':
	print("Result: ", int(number1) * int(number2))

elif operation == '4':
    print("Result: ", int(number1) / int(number2))
else:
    print("Invalid operation")
