for i in range(1, 51):
    if i % 2 == 0:
        print(i)

print("\n")

numbers = [10, 24, 45, 95, 2, 34, 67]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number in the list is: {largest}")

print("\n")

for i in range(5, 51, 5):
    print(i)