# script.py
import os

# Define the path to the file inside the container
file_path = '/data/sample.txt'

# Read and print the content of the file
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:", content)
else:
    print(f"File {file_path} does not exist.")
