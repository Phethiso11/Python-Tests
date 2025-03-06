 # This function creates a new directory if it doesn't already exist.
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created")
    else:
        print(f"Directory {directory} already exists")
# This function creates a new file if it doesn't already exist.

def create_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("")
        print(f"File {file_path} created")
    else:
        print(f"File {file_path} already exists")
# This function writes a string to a file.
