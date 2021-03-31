# When we want some data we import files it may be json, csv, txt file
# Download dictionary json file from internet (It's a large file)
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

# print(data["smog"])  # meaning of smog will be printed

def translate(word):
    word = word.lower()
    if word in data:              # checking for smallcase input smog
        return data[word]
    elif word.title() in data:     # for Smog
        return data[word.title]
    elif word.upper() in data:
        return data[word.upper]    # for USA
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])  # %s is string formatting
        decide = input("Press y for yes & n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return print("Word doesn't exist in this dictionary")
        else:
            return print("Enter just y or n")

    else:
        print("Word doesn't exist in this dictionary")


word = input("Enter the word you want to search in dictionary")
output = translate(word)
if type(output) == list:     #interface 
    for item in output:
        print(item)
else:
    print(ouput)

