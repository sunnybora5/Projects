#This program counts all the characters in string.
#Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc.
import collections
#user enters their input.
userInput = input("Enter any word or phrase: ")
#all characyers in the string is counted and printed out
print(collections.Counter(userInput))
