from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad
######### BASIC ENCRYPTION ###########

# Current function arguments (change may be needed in the future)

def encrypt(msg):
    # The key (must be 16 bytes)
    key = b'Sixteen byte key'

    # Set up the AES encryption class
    encCipher = AES.new(key, AES.MODE_ECB)

    msgBytes = msg.encode('utf-8')

    # Pad and then encrypt
    paddedMsg = pad(msgBytes, AES.block_size) #.encode('etf-8', AES.block_size)

    # AES requires plain/cipher text blocks to be 16 bytes
    cipherText = encCipher.encrypt(paddedMsg)


    file1 = open("manager.txt", "w")
    file1.write(str(cipherText) + "\n")

    print("The cipher text that was written to the file was: ", cipherText)


if __name__ == '__main__':
    msg = str(input("Please enter a message to send to encrypt: "))
    encrypt(msg)