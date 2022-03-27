import flask, random, sys, os, flask
from datetime import datetime, date
from flask import *
app = Flask("__app__")

@app.route("/")
def check():
    key = request.args.get("key")
    with open("database.json", "r") as file:
        json_file = json.load(file)
        database = json_file['Data']
        for User in database:
            if User['Key'] == key:
                now = datetime.strptime(str(datetime.now().strftime("%m/%d/%Y")), "%m/%d/%Y").date()
                subtime = datetime.strptime(User['Expiry'], "%m/%d/%Y").date()
                remaining = subtime - now #It's possible to make a minus date, so we can use the RE module to slice the date easier! (soon)
                if now <= subtime:
                    return({"Success": 1, "Username": f"{User['Name']}", "Expiration": f"{User['Expiry']}"})
                elif now > subtime:
                    return({"Success": 0, "Username": f"{User['Name']}", "Expiration": f"Your subscription has expired. Consider Renewing."})
                else:
                    return("timeout?")
            else:
                pass
        else:
            return({"Success": 0, "Error": "User has not been found with this key"})

app.run("0.0.0.0", 80, debug=True)
