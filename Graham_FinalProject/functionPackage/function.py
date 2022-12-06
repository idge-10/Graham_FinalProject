'''
Created on Nov 22, 2022

@author: 123is
'''
import json
from PIL import Image

def encrypted(Encrypt,English,Code):
    with open(file=Encrypt, mode='r') as read_file:
        object = json.load(read_file)
        Coordiates = object[Code]
        print(Coordiates)
        
        English = open(English, "r")
        data = English.read()
        data_into_list = data.split("\n")
        
        for num in Coordiates:
            location = (data_into_list[int(num)])
            print(location)
        
        temp = set(English)
        res = [i for i, val in enumerate() if val in temp]  
        
        
        
        
        
def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None
    

 

'''
def file_path_Encrypt():
    hints = "EncryptedGroupHints.json"
    with open(file=Encrypt, mode='r') as read_file:
        object = json.load(read_file)
        Graham = (object['Graham'])
        output_json = json.loads(Graham)
    for i in output_json:
        print (i)
        for k in output_json[i]:
            print (k)
# maybe something like this to parse the data to pair the encrypted data with the
# text file?
def parseJsonData(Graham):
    output_json = json.loads(Graham)
    for i in output_json:
        print (i)
        for k in output_json[i]:
            print (k)

def file_path_English():
    English = open("English.txt")
    file_contents2 = English.read()
    print (file_contents2)
    English.close()
   ''' 