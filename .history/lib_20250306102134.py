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

def write_to_file(file_path, content):
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write(content + "\n")
        print(f"Content added to {file_path}")
    else:
        print(f"File {file_path} not found")
# This function reads the contents of a file.

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
        print(f"File content:\n{content}")
    else:
        print(f"File {file_path} not found")
# This function deletes a file.

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted")
    else:
        print(f"File {file_path} not found")
# This function deletes a directory.

def delete_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Directory {directory} deleted")
    else:
        print(f"Directory {directory} not found")
# This function renames a file.
