import json, random, sys, os
from datetime import datetime, date

supplieddata = str(input("Please enter your key: "))
with open("database.json", "r") as file:
    json_file = json.load(file)
    database = json_file['Data']
    for Userz in database:
        if Userz['Key'] == supplieddata:
            now = datetime.strptime(str(datetime.now().strftime("%m/%d/%Y")), "%m/%d/%Y").date()
            subtime = datetime.strptime(Userz['Expiry'], "%m/%d/%Y").date()
            remaining = subtime - now
            if now <= subtime:
                print(f"Welcome {Userz['Name']}, your subscription is valid, Remaining: {remaining}")
                break
            elif now > subtime:
                print("Oopsie, your subscription expired. Consider renewing.")
            else:
                print("You somehow triggered an error. lmfao")
        else:
            pass
    else:
        print("It seems like you inputted a key that doesn't match with any entry in the database.")
        sys.exit()
print("Hello, you're now authenticated. Only cool people should be able to see this")