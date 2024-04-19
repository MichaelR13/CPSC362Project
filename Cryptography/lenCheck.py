def lengthCheck (key):
    if len(key) < 16:
        print ("The key must be 16 characters.")
    if len(key) > 16:
        print ("The key must be 16 characters.")

if __name__ == '__main__':
    key = str(input("Please enter a key (Leave blank for default key): "))

    lengthCheck(key)