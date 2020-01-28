# special libary which can be used for comparison between string objects
import difflib
from difflib import get_close_matches
# mporting module for json files
import json 
 # loading file with database to the python code and saving it into variable data 
data = json.load(open("data.json"))

# creating function to find proper definition of the given word
def translate(word):
    """ Main function of the game responsible for translation of the words """
    if word in data.keys():
        return  data[word]

    elif word.title()  in data.keys():
        return  data[word.title()]        

    elif word.upper() in data.keys():
        return  data[word.upper()]

    elif len(get_close_matches(word,data.keys())) > 0:
        number = len(get_close_matches(word,data.keys(), n = 3 , cutoff = 0.7))
        x = [x for x in range(number)]
        for i in x:
            answer = input("Did you mean %s instead? yes/no:  " % (get_close_matches(word,data.keys()))[i])
            if answer == "yes":
                return data[get_close_matches(word,data.keys())[i]]
            elif answer == "no":
                continue
            else:
                break
        print("Sorry we do not know what do you want")    
    else:
         print("Sorry there is no such word")

while True:
    # Main loop of the dictionary responsible for displaying the results 
    word = input("Enter Word:  ").strip().lower()
    output = translate(word)
    if type(output) == list:
        for d in output:
            print(d) 
    elif type(output) == str:
        print(output)





        




