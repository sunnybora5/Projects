
#boolean variables
Temp = False
Week = False 
Sunny = False

#User input data
check_temp = input ( "Is the tempreture greater than 20 degrees? (YES or NO) ")

if check_temp == "YES":
    Temp = True
    
    
check_week = input ("\nIs it the weekend? (YES or No) ")

if check_week == "YES":
    Week = True 

   
check_sunny = input ("\nIs it sunny ? (YES or NO) ")

if check_sunny == "Yes":
    Sunny = True
    
#Selection of possible  Outfits for user
    
if Temp == True:
    wear1 = "short sleeve shirt"

else:
    wear1 = "long  sleeve shirt"
    

if Week == True:
    wear2 = "shorts"
else:
    wear2 = "jeans"
    
    
if Sunny == True:
    wear3 = "cap"
else:
    wear3 = "rain coat"

print ("\n Your outfit will be " + wear1 + "," + wear2 + " and " + wear3 + ".") 
    
    
    
        

    
