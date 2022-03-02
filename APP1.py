import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(key):
    key=key.lower()

    if key in data:
        return data[key]

    elif len(get_close_matches(key,data.keys()))>0:
        return "Did you mean %s instead?" %get_close_matches(key,data.keys())[0]
    
    else:
        return "Word not found!"

word=input("Enter the Word to be searched : ")

print(meaning(word))