from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt():
    # open file
    with open('manager.bin') as f:
        read_line = f.readline().strip('\n')
        split_list = delimiter(read_line)
        result = decode(split_list)
        if result:
            print("The message in the file was:", result)
        else:
            print("No data found in the file.")

#delim into a list and pass the list into decrypt to get csv file
def delimiter(line):
    splitWords = line.split('|')
    splitWords.pop()
    return splitWords
    
def decode(lst):
    key = b'Sixteen byte key'
    final_list = []

    for item in lst:
        try:
            # Convert the string representation of bytes back to bytes
            encrypted_data = eval(item)

            # Set up the AES decryption cipher
            dec_cipher = AES.new(key, AES.MODE_ECB)

            # Decrypt the data
            decrypted_data = dec_cipher.decrypt(encrypted_data)

            # Remove padding from the decrypted data
            unpadded_data = unpad(decrypted_data, AES.block_size)

            final_list.append(unpadded_data.decode('utf-8'))    # Convert the bytes back to a string
        except Exception as e:
            print("Error decrypting data:", e)

    return final_list

if __name__ == '__main__':
    decrypt()