# When we want some data we import files it may be json, csv, txt file
# Download dictionary json file from internet (It's a large file)
import json

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
    
    

    else:
        print("Word doesn't exist in this dictionary")


word = input("Enter the word you want to search in dictionary")
output = translate(word)
if type(output) == list:     #interface 
    for item in output:
        print(item)
else:
    print(ouput)


