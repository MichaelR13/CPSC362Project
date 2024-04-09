from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad
######### BASIC ENCRYPTION ###########

# Current function arguments (change may be needed in the future)

def encrypt(key,*info):

    # The key (must be 16 bytes)
    if key == "":
        key = b'Sixteen byte key'
    print(info)
    encryptInfo(info,key)
    

def encryptInfo(infoList, key):
    # Set up the AES encryption class
    file1 = open("manager.bin", "a")

    for i in infoList:
        encCipher = AES.new(key, AES.MODE_ECB)

        msgBytes = i.encode('utf-8')

        # Pad and then encrypt
        paddedMsg = pad(msgBytes, AES.block_size) #.encode('etf-8', AES.block_size)

        # AES requires plain/cipher text blocks to be 16 bytes
        cipherText = encCipher.encrypt(paddedMsg)

        
        file1.write(str(cipherText) + "|")
        print("The cipher text that was written to the file was: ", cipherText)
    
    file1.write('\n')
    file1.close()
    


if __name__ == '__main__':
    username = str(input("Please enter your username: "))
    password = str(input("Please enter your password: "))
    website = str(input("Please enter your website: "))
    key = ""
    encrypt(key, username, password, website)