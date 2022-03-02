import json

data = json.load(open("data.json"))

def meaning(key):
    key=key.lower()

    if key in data:
        return data[key]
    else:
        return "Word not found!"

word=input("Enter the Word to be searched : ")

print(meaning(word))