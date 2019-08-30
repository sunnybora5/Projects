#this program checks if a word is a palindrome
string = input("Enter any word: ").lower()
#Reverses the input by user.
revString = string[::-1]
#checks if the input is a palindrome and prints that its a palindrome.
if string == revString:
    print("This is a palindrome")
#If its not its prints that its not.
else:
    print("This is not a palindrome")
