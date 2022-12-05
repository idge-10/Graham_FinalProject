"""
Name: Isaac Hedges, Ben Truax, Jack Hutz
email: hedgesic@mail.uc.edu, truaxbp@mail.uc.edu
Assignment: Assignment12
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Citations:
Anything else that's relevant: 
"""
from functionPackage.function import *
import json  #built in, no pip required (if needed, uses "jsons" import)
import requests
from functionPackage.function import file_path_English
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
# import requests
from io import BytesIO
# This one is in Main.py only
from image_functions import *
# file_path_English()

# file_path_Encrypt()
my_image = load_image("bridge.jpg")
my_image.show(my_image)
    


'''
# find the files
file_path_English = "EncryptedGroupHints.json"
file_path_Encrypted = "EncryptedGroupHints.json"

# open the files
with open(file=file_path_Encrypted, mode='r') as read_file:
    object = json.load(read_file)
with open(file=file_path_Encrypted, mode='r') as read_file:
    object = json.load(read_file)
    print(object['Graham'])
    
if object['Graham']:
 '''   
    
