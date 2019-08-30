#This program prints out all times table of the number the user enters all times tables of the enterd
#number mu;tiplied up to 12.

print("\t\t Times table generator")
digit = int(input("\nEnter digit here: "))

#This code restrics the ouput so that only numbers from 1-12 will print
for i in range (1, 13) :
    #This code checks if the numbers can fully be digited by digit(user inputed number)
        print (str(i), "x" , digit , " = " ,digit*i)
        #This code calculates the multiples
          

#this program checks for leap years.
print("\n\n\n")
print("\t\t Leap year generator")
#The user inputs.
year = int (input("\nEnter a year: "))
number_years = int(input("How many years"))

#This code creates a restriction so the year prints and the code ends a number before the final year.
for i in range(year,year+number_years+1):
    if (i % 4) == 0 :
        print("this is a leap year",i)
        
    else:
        print("This is not a leap year",i)
        
    



          
   

        

         
        
    
        
            
                   
        


  
            
    
    
5
