import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(key):
    key=key.lower()

    if key in data:
        return data[key]

    elif len(get_close_matches(key,data.keys()))>0:
        rec= input("Did you mean %s instead? Enter 'Y' if yes or 'N' if no." %get_close_matches(key,data.keys())[0])
        
        if rec=="Y":
            return data[get_close_matches(key,data.keys())[0]]
        elif rec=="N":
            return "Word not found!"
        else:
            return "Invalid Entry"

    else:
        return "Word not found!"

word=input("Enter the Word to be searched : ")

output=meaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)