from pathlib import Path
from decryption import delimiter
from decryption import decode

def fileExist(key):
    # open file
    my_file = Path("manager.bin")
    if my_file.is_file():
    # if file does not exist in path
        print("file exists")
    # file exists
        with open(my_file) as f:
            first_line = f.readline().strip('\n')
            split_list = delimiter(first_line)
            result = decode(split_list, key)
        if result != ["empty"]:
            return True
    return False


if __name__ == '__main__':
    key = str(input("Please enter a key (Leave blank for default key): "))

    fileExist(key)