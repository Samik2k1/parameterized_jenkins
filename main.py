import sys


def process_file(file_path):
    with open(file_path, 'r') as file:
        fileContent = file.read()
        print(fileContent + "\n")


if __name__ == '__main__':
    print("This is a program to take the file name as  show the contents of the uploaded file")
    file_path = sys.argv[1]
    process_file(file_path)
