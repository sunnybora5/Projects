#This program removes specific characters from a string
#User enters input
userInput = input("Enter any phrase or word: ")
userReplacer = input ("Enter any variable\s you want to remove from your word(separated by comma()): ").lower()

#The code repeats so thta the process can be run more than once so thta each chracter can be removed throughout the phrase.
for i in userReplacer:
   if i in  userInput:
     #this code adds the all the characters the user wants to remove so thta its possible for user to add more than character to be removed.
     # the replace(i,'') replaces the characters eneterd by the user with an empty space 
     userInput =  userInput.replace(i,'')
#End result prints      
print(userInput)
