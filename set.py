unique_numbers = set([1, 2, 3, 4, 5, 3, 2, 6, 7, 8])


print("Unique Numbers:", unique_numbers)

print("Sum of Unique Numbers:", sum(unique_numbers))

print("Maximum Number:", max(unique_numbers))
print("Minimum Number:", min(unique_numbers))

unique_numbers.remove(max(unique_numbers))
print("Updated Set after Removing Largest Number:", unique_numbers)

new_numbers = {4, 5, 6, 9, 10}

print("Union:", unique_numbers.union(new_numbers))

print("Intersection:", unique_numbers.intersection(new_numbers))

print("Difference (unique_numbers - new_numbers):", unique_numbers.difference(new_numbers))

print("Symmetric Difference:", unique_numbers.symmetric_difference(new_numbers))
