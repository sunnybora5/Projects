# This program changes the casing of alternate letters .

# user inputs a string/ strings.
wordUser = input("Enter word here: ")


# the strings are matched with their posistion to integer.
# the program reads the position of the letters of the entered word.
for (num, letter) in enumerate(wordUser):
    # This checks for all the even letters of the entered string.
    # if num % 2 = 0:
        # your code was missing the second = sign

    if num % 2 == 0:
        print(letter.upper())
    # all odd letters are printed out lower cased.
    else:
        print(letter.lower)
