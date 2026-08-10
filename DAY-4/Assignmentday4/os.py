import os

def list_directory_contents(path="."):
    """Returns a list of files and folders in the specified directory."""
    return os.listdir(path)

# Program execution
files = list_directory_contents(".")
print("Files in current directory:", files)