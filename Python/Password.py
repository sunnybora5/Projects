
print (" How to check if your password is Strong.")

#Variables casted 
haveLegnth = False
upCase = False
lowCase = False
haveNum = False
anwser = False
no_answ = 0

#User enter data for

#Checking password legnth.
check_legnth = input ("\n Does your password contain more than six characters ? (Yes or No) ")
if  check_legnth == "Yes":
        haveLegnth = True
  
# checking for uppercase.
check_upper = input ("\n Does your password contain any uppercase characters ? ( Yes or No) ")
if check_upper == "Yes":
        upCase = True
  
#checking for lowercase.
check_lower = input ("\n Does your password contain any lowercase characters ? (Yes or No) ")
if check_lower == "Yes":
          lowCase = True

# Checking for numerals.
check_num = input ("\n Does password contain any numeral characters ? (Yes or No) ")
if  check_num == "Yes":
         haveNum = True

print ("\n")
# Data confirguration.

if haveLegnth == True:
        print (" Congrats! Your password contains more than six characters. ")
        no_answ += 1
else :
        print (" Unfortunateley your password contains less than six characters. ")


if upCase == True:
        print (" Congrats! Your password contains uppercase characters. ")
        no_answ +=1
else:
        print (" Unfortunately Your password contains no uppercase characters. ")

        
if lowCase == True:
        print (" Congrats! Your password contains lowercase characters. ")
        no_answ +=1
else:
        print (" Unfortunately your password contains no lowercase characters")


if haveNum == True:
        print (" Congrats! Your password contains numeral characters. ")
        no_answ +=1
else:
        print (" Unfortunately your password contains no numeral characters. ")
        
# Final confiragation to check if password has alleast three of the four variables


if no_answ >= 3:
        answer = True
        print ("\n Success! Your password is Strong. ")
elif no_answ <3:
        print ("\n Try again! Your password is weak. ")
        






 

 
 
  
  
  
