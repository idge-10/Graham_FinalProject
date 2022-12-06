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



from functionPackage.function import *
# printing statement for location
Code = encrypted('EncryptedGroupHints.json','english.txt','Graham')
# showing the image taken at location
my_image = load_image("Team_Graham_Picture.jpg")


