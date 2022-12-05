'''
Created on Nov 22, 2022

@author: 123is
'''
import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
# import requests
#from io import BytesIO

def file_path_Encrypt():
    Encrypt = "EncryptedGroupHints.json"
    with open(file=Encrypt, mode='r') as read_file:
        object = json.load(read_file)
        print(object['Graham'])
        
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
def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None
   
    