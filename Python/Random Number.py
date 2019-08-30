import random

    
winner = str(random.randrange(10,99))

user_win = str(input("\nEnter any two digit number from (10 to 99) :"))

#Random number and User input casted to characters is they can match.
winA = winner[0]
winB = winner[1]
userA = user_win[0]
userB = user_win[1]


#This states if the user input is same as random
if userA == winA and userB == winA:
    print ("Congratulations you have an exact match you win R10 000.00\n")
   
#This show if the user input is same but different position. 
elif userA == winB and userB == winA:
    print ("\nCongartulation you have all digits you R5 000.00\n")
    
#This shows if user input is atleast one character correct.    
elif (userA == winA or userB == winB) or (userA == winB or userB == winA):     
    print ("\nCongratulations you have one correct digit, you win R1 000.00")
    

else:
    print ("\nSorry no match")
    

print ("Here is the winning number",winner)


                  
