#!/usr/bin/env python3

# farms dictionary
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},{"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for function1 in farms:
    if function1.get('name') == "NE Farm":
        print(function1.get('agriculture'))


inputFarm = input("Pleae choose (NE Farm, W Farm or SE Farm) a farm to display its plant/animal \n >")

for function2 in farms:
    if function2.get('name') == inputFarm:
        print(function2.get('agriculture'))
        break

inputFarm = input("Pleae choose (NE Farm, W Farm or SE Farm) a farm to display its plant/animal \n >")

for function3 in farms:
    if function3.get('name') == inputFarm:
        if inputFarm == "SE Farm":
            onlyAnimal = function3.get('agriculture')
            print(onlyAnimal[0])
            break
        else:
            print(function3.get('agriculture'))
            break
