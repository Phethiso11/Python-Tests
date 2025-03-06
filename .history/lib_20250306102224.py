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

def rename_file(old_file_path, new_file_path):
    if os.path.exists(old_file_path):
        os.rename(old_file_path, new_file_path)
        print(f"File {old_file_path} renamed to {new_file_path}")
    else:
        print(f"File {old_file_path} not found")
# This function renames a directory.

def rename_dir(old_directory_path, new_directory_path):
    if os.path.exists(old_directory_path):
        os.rename(old_directory_path, new_directory_path)
        print(f"Directory {old_directory_path} renamed to {new_directory_path}")
    else:
        print(f"Directory {old_directory_path} not found")
# This function copies a file.

def copy_file(old_file_path, new_file_path):
    if os.path.exists(old_file_path):
        shutil.copy(old_file_path, new_file_path)
        print(f"File {old_file_path} copied to {new_file_path}")
    else:
        print(f"File {old_file_path} not found")
# This function copies a directory.

def copy_dir(old_directory_path, new_directory_path):
    if os.path.exists(old_directory_path):
        shutil.copytree(old_directory_path, new_directory_path)
        print(f"Directory {old_directory_path} copied to {new_directory_path}")
    else:
        print(f"Directory {old_directory_path} not found")
# This function moves a file.

def move_file(old_file_path, new_file_path):
    if os.path.exists(old_file_path):
        shutil.move(old_file_path, new_file_path)
        print(f"File {old_file_path} moved to {new_file_path}")
    else:
        print(f"File {old_file_path} not found")
# This function moves a directory.

def move_dir(old_directory_path, new_directory_path):
    if os.path.exists(old_directory_path):
        shutil.move(old_directory_path, new_directory_path)
        print(f"Directory {old_directory_path} moved to {new_directory_path}")
    else:
        print(f"Directory {old_directory_path} not found")
# This function lists all files in a directory.

def list_files(directory_path):
    if os.path.exists(directory_path):
        for file in os.listdir(directory_path):
            print(file)
    else:
        print(f"Directory {directory_path} not found")
# This function lists all directories in a directory.

def list_directories(directory_path):
    if os.path.exists(directory_path):
        for directory in os.listdir(directory_path):
            if os.path.isdir(os.path.join(directory_path, directory)):
                print(directory)
    else:
        print(f"Directory {directory_path} not found")