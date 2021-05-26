#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint
import os
AOIF = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    pprint.pprint(got_dj)

    questionNumber = int(input("Choose a question number between 1 and 10\n")) - 1

    answerInput = input(f'The questrion for you is - {got_dj["results"][questionNumber].get("question")} True or False?\n')
    
    if got_dj["results"][questionNumber].get("correct_answer").upper() == answerInput.upper():
        print("Correct Answer")
    else:
        print(f'Wrong Answer, the correct answer is {got_dj["results"][questionNumber].get("correct_answer")}')

if __name__ == "__main__":
    os.system('clear')
    main()

