import googlemaps
from datetime import datetime
import re

def direction():
    #input API key
    #gmaps = googlemaps.Client()

    print("Welcome to the directions feature! Enter any address and directions to campus will be provided.")
    #get address from user
    address = input("Please enter your address: ")

    #check address is valid
    valid_address = False
    while(valid_address == False):
        try:
            # Request directions via walking
            directions_result = gmaps.directions(address,
                                        "The University of British Columbia - Okanagan Campus",
                                        mode="walking")
            valid_address = True
        except:
            address = input("The address entered is not valid. Please try again: \n")

    #define html cleaner
    CLEANR = re.compile('<.*?>') 

    #Output directions
    no_stop = True
    print("The following steps are your directions:")
    i = 0
    while(no_stop == True):
        try:
            distance1 = directions_result[0]['legs'][0]['steps'][i]['distance']['text']
            step1 = cleantext = re.sub(CLEANR, '', directions_result[0]['legs'][0]['steps'][i]['html_instructions'])
            output1 = (f"Walk for {distance1} and then {step1}")
            print(output1)
        except:
            no_stop = False
        i = i + 1