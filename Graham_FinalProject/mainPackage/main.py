"""
Name: Isaac Hedges, Ben Truax, Jack Hutz
email: hedgesic@mail.uc.edu, truaxbp@mail.uc.edu
Assignment: Assignment11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Writing using an API to find unique information
Citations:
Anything else that's relevant: 
"""

import json  #built in, no pip required (if needed, uses "jsons" import)
import requests

file = open('EncryptedGroupHints.json')
data = json.load(file)



'''
json.load('EncryptedGroupHints.json')
json_string = response.content


# Parse the results
parsed_json = json.loads(json_string) # Now we have a python dictionary

# Check on parsed results
print(parsed_json)
'''