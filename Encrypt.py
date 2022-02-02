import os
#File Name
testfile = 'TestFile.txt'

#File Location
filelocation = '/home/brinda/TestFile.txt'

path = os.path.join(testfile, filelocation)

openfile = open(path)
lines = openfile.read()


#Encrypt 
def Caesar_Cipher(lines, key):
    encrypted = ''
    for c in lines:
        if c == ' ':
            d = ' '

        else:
            d = chr(ord(c) + key)

        encrypted = encrypted + d
        
    return encrypted


print(Caesar_Cipher(lines, 2))
