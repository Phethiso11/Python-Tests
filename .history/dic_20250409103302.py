# Create a dictionary with fruit names as keys and their prices as values
fruits = {
    "apple": 3.5,
    "banana": 1.2,
    "cherry": 5.0,
    "date": 3.5,
    "elderberry": 7.0
}

# Convert the dictionary keys into a list of fruit names
fruit_names = list(fruits.keys())
print("List of fruit names:", fruit_names)

# Convert the dictionary values into a set to get unique prices
unique_prices = set(fruits.values())
print("Set of unique prices:", unique_prices)

# Convert the entire dictionary into a list of tuples (fruit, price)
fruit_tuples = list(fruits.items())
print("List of tuples (fruit, price):", fruit_tuples)