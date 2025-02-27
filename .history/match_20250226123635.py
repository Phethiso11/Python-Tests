def get_day_of_week(day_number):
    match day_number:
        case 1:
            return "The day is Monday"
        case 2:
            return "The day is Tuesday"
        case 3:
            return "The day is Wednesday"
        case 4:
            return "The day is Thursday"
        case 5:
            return "The day is Friday"
        case 6:
            return "The day is Saturday"
        case 7:
            return "The day is Sunday"
        case _:
            return "Invalid day number"

def main():
    try:
        day_number = int(input("Enter a number (1-7): "))
        print(get_day_of_week(day_number))
    except ValueError:
        print("Please enter a valid number.")
    except Stri:
        print("An error occurred.")

if __name__ == "__main__":
    main()