#!/usr/bin/env python3

fruitcompaniesDict= [
                    {"name":"Zesty","employees":["Ajay","Ashfaq","Bob","Brian","Chad F.", "Chad H."]},
                    {"name":"Ripe.ly","employees":["Eric","Gibran", "Chad","Idris","Juan","Julian"]},
                    {"name":"FruitBee","employees":["Kulwinder","Lalit","Chad","Michael","Milford","Scott"]},
                    {"name":"JuiceGrove","employees":["Chad","Srini","Srinivasa","Vasanti","Vimal"]}]
companyList=[]
doItAgain = "Y"

# excellent use of a while loop!
# now, you only want the loop to run again UNLESS they type 2, right?
# then consider using this:
#while doItAgain < "2":
while doItAgain == "Y":
    for displayWork in fruitcompaniesDict:
        print(f"Following people who work for {displayWork.get('name')} are  {displayWork.get('employees')}")
        companyList.append(displayWork.get('name'))

    choose_Company = input(f" Choose a company from {companyList}: ")
    for displayWork in fruitcompaniesDict:
        if displayWork.get('name').lower() == choose_Company.lower():
            print(f"Following people who work for {choose_Company} are {displayWork.get('employees')}")
  
    choose_Company = input(f" Choose a company from {companyList}: ")
    for displayWork in fruitcompaniesDict:
        if displayWork.get('name').lower() == choose_Company.lower():
            for displayExcludeChad in displayWork.get('employees'):
                if displayExcludeChad != "Chad F.":
                    print(f"Following people who work for {choose_Company} are {displayExcludeChad}")

    doItAgain = input("Do you want to continue (Y / N)?")

