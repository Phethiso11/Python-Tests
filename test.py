def sort_characters(input_string):
    
    characters = input_string.split(',')
    
    characters.sort()

    sorted_characters = ','.join(characters)
    return sorted_characters

if __name__ == "__main__":
    input_string = input("Enter characters separated by commas: ")
    sorted_string = sort_characters(input_string)
    print("Sorted characters:", sorted_string)