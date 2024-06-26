from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(key):
    # open file
    file1 = open('manager.bin', 'r')
    Lines = file1.readlines()
    resultList = []
    for f in Lines:
        read_line = f.strip('\n')
        split_list = delimiter(read_line)
        result = decode(split_list, key)
        
        if result:
            print("The message in the file was:", result)
            resultList.append(result)
    return resultList


def delimiter(line):
    # Split the line into a list
    splitWords = line.split('|')
    splitWords.pop(0)
    return splitWords
    
def decode(lst, key):

    key = key.encode('utf-8')
    
    final_list = []

    for item in lst:
        try:
            # Convert the string to byte array
            encrypted_data = eval(item)

            # Set up the AES decryption cipher
            dec_cipher = AES.new(key, AES.MODE_ECB)

            # Decrypt the data
            decrypted_data = dec_cipher.decrypt(encrypted_data)

            # Remove padding from the decrypted data
            unpadded_data = unpad(decrypted_data, AES.block_size)

            # Append data to the end of the list
            final_list.append(unpadded_data.decode('utf-8'))    # Convert the bytes back to a string

        except Exception as e:
            print("Error decrypting data:", e)
            return False

    return final_list

if __name__ == '__main__':
    key = str(input("Please enter a key (Leave blank for default key): "))

    decrypt(key)