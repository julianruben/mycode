#!/usr/bin/env python3


muhammadDict = {"name":
                    {"birth":"Cassius Clay",
                     "current":"Muhammad Ali"},
                "contact":
                    {"phone":"333-444-5555",
                     "email":"thebest@boxing.com"},
                "favorites":
                    {"number":56,
                        "food":
                            {"baked chicken":3.5,
                            "mac and cheese":4.5,
                            "spinach":2,
                            "green peas":2},
                        "drink":
                            {   "adult":["none"],
                                "nonadult":["Mr. Champ soda"]
                            }
                    }
                }

foodList = muhammadDict.get('favorites').get('food').keys()
foodCost = muhammadDict.get('favorites').get('food').values()
print ("Muhammad Ali's favorite foods are: \n")
for fList in foodList:
    print(fList)



totalCost = 0
for fCost in foodCost:
    totalCost += fCost

print(f"Muhammad Ali's favorite food cost is = {totalCost}")
