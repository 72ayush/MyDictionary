import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif(len(get_close_matches(word, data.keys()))>0):
        yn = input("Sorry, this word %s does not exists, Did you mean %s instead? Enter 'Y' for Yes and 'N' for No: " % (word, get_close_matches(word, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Sorry, This word does not exists, please recheck it."
        else:
            return "We did not understand your entry."

    else:
        return "Sorry, This word does not exists, please recheck it."

word = input("Input a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
