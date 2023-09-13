"""EX01 - Chardle - A cute step toward Wordle.""" 
__author__ = "730698705"

user_word = input("Enter a 5-character word: " ) 
if len(user_word) != 5: 
    print("Error: Word must contain 5 words") 
    exit()
user_letter = input("Enter a single character: " )  
if len(user_letter) != 1: 
    print("Error: Character must be a single character") 
    exit()
print("Searching for " + user_letter + " in " + user_word)   

num_instances: int = 0
if user_letter == user_word [0]: 
    print( user_letter + " found at index 0 ") 
    num_instances = num_instances + 1
if user_letter == user_word [1]:
    print( user_letter + " found at index 1")  
    num_instances = num_instances + 1
if user_letter == user_word [2]: 
    print( user_letter + " found at index 2 ") 
    num_instances = num_instances + 1
if user_letter == user_word [3]: 
    print( user_letter + " found at index 3 ") 
    num_instances = num_instances + 1 
if user_letter == user_word [4]: 
    print( user_letter + " found at index 4 ")  
    num_instances = num_instances + 1  

if num_instances == 0: 
    print("No instances of ", user_letter, " found in ",  user_word) 
elif num_instances == 1: 
    print(num_instances, "instances of ", user_letter, "found in", user_word)
elif num_instances > 1: 
    print(num_instances,  "instances of",  user_letter,  "found in",  user_word)