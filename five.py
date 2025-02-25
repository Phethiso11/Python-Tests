def isLongerThan(s):
    return len(s) > 5

def main():
    try:
        user_input = input("Enter a string: ")
        if isLongerThan(user_input):
            print("True")
        else:
            print("False")
    except:
        print("Error: Invalid input")
    finally:
        print("End of program")

if __name__ == "__main__":
    main()