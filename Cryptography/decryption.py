from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt():
    # open file
    with open('manager.txt') as f:
        first_line = f.readline().strip('\n')
        finalMsg = decodeLine(first_line)
        

    return finalMsg


def decodeLine(line):
    # The key (must be 16 bytes)
    key = b'Sixteen byte key'


    # This decode function does not work.
    # Michael pls try and fix.
    # -Kyle

    # Set up the AES encryption class
    encCipher = AES.new(key, AES.MODE_ECB)

    decryptedMsg = unpad(encCipher.decrypt(line), AES.block_size).decode('utf-8')
    # Pad and then encrypt
    #unpaddedMsg = unpad(decryptedMsg, AES.block_size)

    return decryptedMsg



if __name__ == '__main__':
    print("The message in the final was: ", decrypt())
