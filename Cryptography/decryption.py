from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt():
    # open file
    with open('manager.txt') as f:
        readLine = f.readline().strip('\n')
        splitList = delimiter(readLine)
        returnedList = decode(splitList)




#delim into a list
#pass the list into decrypt to get csv file

def delimiter(line):
    splitWords = line.split('|')
    splitWords.pop()
    return splitWords
    


def decode(seperatedList):
    # The key (must be 16 bytes)
    key = b'Sixteen byte key'

    for i in seperatedList:
        # Set up the AES encryption class
        cipher = AES.new(key, AES.MODE_ECB)
        #THIS DOES NOT WORK :(
        decryptedMsg = cipher.decrypt(i)

        # Pad and then encrypt
        unpaddedMsg = unpad(decryptedMsg, 16).decode()

        print(unpaddedMsg)



if __name__ == '__main__':
    print("The message in the file was: ", decrypt())