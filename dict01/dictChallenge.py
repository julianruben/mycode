#!/usr/bin/env python3

heroes=  {
          "wolverine":
                {"real name": "James Howlett",
                 "powers": "regeneration",
                 "archenemy": "Sabertooth",},
          "harry potter":
                {"real name": "Harry Potter",
                 "powers": "magic",
                 "archenemy": "Voldemort",},
          "captain america":
                {"real name": "Steve Rogers",
                 "powers": "frisbee shield",
                 "archenemy": "Hydra",}
         }
doItAgain = "Y"

# excellent use of a while loop!
# now, you only want the loop to run again UNLESS they type 2, right?
# then consider using this:
#while doItAgain < "2":
while doItAgain == "Y":
    char_name = input(" Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)?").lower()
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)?").lower()
    if heroes.get(char_name) is not None:
        value = heroes[char_name].get(char_stat)
        print(f"{char_name.title()} 's {char_stat} is: {value}")
    else:
        print("The character you have given is not present")
    doItAgain = input("Do you want to continue (Y / N)?")
