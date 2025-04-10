fruits = {
    "apple": "M3.5 per kg",
    "banana": "M1.2 per kg",
    "cherry": 5.0,
    "date": 3.5,
    "elderberry": 7.0
}

fruit_names = list(fruits.keys())
print("List of fruit names:", fruit_names)

unique_prices = set(fruits.values())
print("Set of unique prices:", unique_prices)

fruit_tuples = list(fruits.items())
print("List of tuples (fruit, price):", fruit_tuples)
