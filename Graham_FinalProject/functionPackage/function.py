"""
Name: Isaac Hedges, Ben Truax, Jack Hutz, Alyssa Hughes
email: hedgesic@mail.uc.edu, truaxbp@mail.uc.edu, hutzjm@mail.uc.edu, hugheah@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Decrypting txt and json file and uploading image
Citations: https://www.google.com/search?q=what+is+split+in+python&oq=what+is+split+in+&aqs=chrome.0.0i512l10.2651j0j7&sourceid=chrome&ie=UTF-8
Anything else that's relevant: 
"""
import json
from PIL import Image


# creating a function to decrypt
def encrypted(Encrypt,English,Code):
    # reading the EncryptedGroupHints.json file
    with open(file=Encrypt, mode='r') as read_file:
        File = json.load(read_file)
        Coordinates = File[Code]
    # reading the english.txt file   
        English = open(English, "r")
        data = English.read()
    # using split to turn string into list
        dataSet = data.split()
    # parsing files to find the decrypted location   
        location = ""
        for num in Coordinates:
            location += (dataSet[int(num)]) + " "
        print(location)
 # creating function to load the image taken at decrypted location               
def load_image( filename ) :
    try:
        # opening image
        myimage = Image.open(filename)
        # rotating image
        rotate_image = myimage.rotate(270)
        # showing image
        rotate_image.show(rotate_image)
    except:
        return None
    