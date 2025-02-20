def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    numbers = []
    for i in range(4):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    
    average = calculate_average(numbers)
    print(f"The average of the four numbers is: {average}")

if __name__ == "__main__":
    main()