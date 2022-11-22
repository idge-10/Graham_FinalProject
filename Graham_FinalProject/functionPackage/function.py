'''
Created on Nov 22, 2022

@author: 123is
'''
import json

def file_path_Encrypt():
    Encrypt = "EncryptedGroupHints.json"
    with open(file=Encrypt, mode='r') as read_file:
        object = json.load(read_file)
        print(object['Graham'])

'''
def file_path_Encrypt():
    Encrypt = open("EncryptedGroupHints.json")
    file_contents1 = Encrypt.read()
    print (file_contents1["Graham"])
    Encrypt.close() 
'''

def file_path_English():
    English = open("English.txt")
    file_contents2 = English.read()
    print (file_contents2)
    English.close()
    
   
    