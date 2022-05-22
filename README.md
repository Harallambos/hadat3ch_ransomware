# hadat3ch_ransomware
### THERE ARE 3 FILES IN THIS REPOSITORY

<br>

1. hadat3ch-ransomware.py (This file is the script that encrypts the files that are in the same folder with the script. It excludes itseld the decryption script and another file that is created when the decryption script is executed and this new file will be the encryption/decryption key file.)
2. hadat3ch-ransomware-decrypt.py (This script will decrypt all the encrypted files using the key file)
3. Test.txt (this is a test files so we can see that during the encryptionand decryption the file content changes)

<br>
<br>
RECUIREMENTS
<br>
# ---------------------------------------------------------------------------------------
<br>
You need to have python or python3 installed on your linux macchine in order to run those scripts.
<br>
# ---------------------------------------------------------------------------------------
<br>
<br>
EXECUTION
<br>
Please check first the content of the Test.txt file. 
<br>
contaent: "This is a test file and it's content will be used to see if the files is decrypted or encrypted form the "hadat3ch-ransomware.py" script which will encrypt it and from the "hadat3ch-ransomware.py" which will decrypt it.
"
<br>
<br>
<br>
{ENCRYPTION}
<br>
Please download the files and put them in the same folder. Go to your terminal and make sure you have python installed in your system.
<br>
After all files are in the same folder open a terminal and navigate to the folders path. Then to run the first script type:
<br>
# -------------------------------
<br>
python3 hadat3ch-ransomware.py
<br>
# -------------------------------
<br>
<br>
<br>
{DECRYPTION}
<br>
If you check the content of the Test.txt file you will see that it is now encrypted and the content is random letters and numbers.
<br>
To decrypt your file now run the decryption script. Go to terminal and type:
<br>
# -------------------------------------
<br>
python3 hadat3ch-ransomware-decrypt.py
<br>
# -------------------------------------
<br>
<br>
It will ask you to enter the secret phrase which id "hadat3ch" and this will allow you to decrypt the files in the same folder.
