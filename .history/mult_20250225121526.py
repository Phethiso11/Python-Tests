def print_numbers():
    for i in range(1, 51):
        if i % 7 == 0:
            continue
        print(i)

if __name__ == "__main__":
    print_numbers()