from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(key,*info):
    key = key.encode('utf-8')
    print(info)
    returnMsg = encryptInfo(info, key)
    print (returnMsg)

    

def encryptInfo(infoList, key):
    # Set up the AES encryption class
    file1 = open("manager.bin", "a")

    errorCheck = makeStr(infoList, key)

    if errorCheck[0] == "Data successfully written to file":
        file1.write(errorCheck[1])
    
    file1.write('\n')
    file1.close()

    # Return status
    return errorCheck[0]
    
def makeStr(infoList, key):
    tempStr = ""
    try:
        for i in infoList:
            # Set up the AES decryption cipher
            encCipher = AES.new(key, AES.MODE_ECB)

            # Convert the message to byte array
            msgBytes = i.encode('utf-8')

            # Pad and then encrypt
            paddedMsg = pad(msgBytes, AES.block_size)

            # AES requires plain/cipher text blocks to be 16 bytes
            cipherText = encCipher.encrypt(paddedMsg)

            # Add 
            print("The cipher text that was written to the file was: ", cipherText)
            tempStr = tempStr + '|' + str(cipherText)

    except Exception as e:
        return ["Data failed to write to file",tempStr]

    return ["Data successfully written to file", tempStr]

if __name__ == '__main__':
    username = str(input("Please enter your username: "))
    password = str(input("Please enter your password: "))
    website = str(input("Please enter your website: "))
    key = str(input("Please enter a key (Leave blank for default key): "))
    print(len(key))
    encrypt(key, username, password, website)