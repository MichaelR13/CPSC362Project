from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt():
    # open file
    with open('manager.bin') as f:
        readLine = f.readline().strip('\n')
        splitList = delimiter(readLine)
        returnedList = decode(splitList)




#delim into a list
#pass the list into decrypt to get csv file

def delimiter(line):
    splitWords = line.split('|')
    splitWords.pop()
    return splitWords
    
def decode(list):

    key = b'Sixteen byte key'
    finalList = []

    for i in list:
        # Set up the AES encryption class
        decCipher = AES.new(key, AES.MODE_ECB)

        print(i)

        # AES requires plain/cipher text blocks to be 16 bytes
        plainText = decCipher.decrypt(i)

        finalList.append(plainText)

        


if __name__ == '__main__':
    print("The message in the file was: ", decrypt())