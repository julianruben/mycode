#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import os

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character!\n " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        if got_dj["allegiances"]:
            allegiances = requests.get(got_dj.get('allegiances')[0]).json()
            print(f'\nHouse affiliated with the character is : {allegiances["name"]}')

            if got_dj["povBooks"]:
                booklist = requests.get(got_dj['povBooks'][0]).json()
                print('\n List of books they narrate are:')
                linenumber = 1
                for displayname in got_dj["povBooks"]:
                    # display ONLY the name value associated with astro
                    displaybook = requests.get(displayname).json()
                    print(f'{linenumber} - {displaybook["name"]}')
                    linenumber += 1
            else:
                print("\nThe character does not narrage any books")
        else:
            print("\nNo House Affliated with this character")
continueAgain = 'Y'
if __name__ == "__main__":
    while continueAgain.upper() == "Y":
        os.system('clear')
        main()
        continueAgain = input("\nDo you want to continue Y or N: ")

