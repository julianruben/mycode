#!/usr/bin/python3

import yaml

def main():
    gamejson = [{
  "Hall": {
    "south": "Kitchen",
    "east": "Dining Room",
    "item": "key"
  },
  "Kitchen": {
    "north": "Hall",
    "item": "monster"
  },
  "Dining Room": {
    "west": "Hall",
    "south": "Garden",
    "item": "potion",
    "north": "Pantry"
  },
  "Garden": {
    "north": "Dining Room"
  },
  "Pantry": {
    "south": "Dining Room",
    "item": "cookie"
  }
}]
        
    ## display our Python data (a list containing two dictionaries)
    print(gamejson)
    
    ## Create the YAML string
    yamlstring = yaml.dump(gamejson)
    
    ## Display a single string of YAML
    print(yamlstring)
    
if __name__ == "__main__":
    main()

