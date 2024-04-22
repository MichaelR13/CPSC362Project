def lengthCheck (key):
    if len(key) != 16:
        return False
    else:
        return True

if __name__ == '__main__':
    key = str(input("Please enter a key (Leave blank for default key): "))

    lengthCheck(key)