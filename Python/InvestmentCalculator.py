import math

#User enter their data.
P = float (input("Enter how much you want to invest? R"))
i = float (input("Enter your interest rate? "))
t = float (input("How long will you be investing? "))

interest = input("\nWhat type of investment would you like Simple or Compound interest (Compound or Simple) ? ").lower
()

#Turning "i" variable to percentage e.g r= i divided by a 100.
r = (i/100)
#+ I commented this code out, because its giving a error, please be careful about these Thanks
#possilbe outcomes depending on user. So that the input entered by the user can be processed.
#The data is stored.
if interest == "simple":
    formula = P*(1+r*t)
    
elif interest == "compound":
    formula = P*((1+r)**t)
    
#Formula rounded off so that is readible by user.
rounded = round(formula,2)

print ("\nYour investment \nR" + str(rounded))
