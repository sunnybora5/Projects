#This is a empty lis to store all the data eneterd by the user     
newlist = list()
name = 0

#Restriction set for if input is equal to "John" and the loop stops and prints list of possible inputs.
while name != "john" :
    #Input of user loops over and over for restriction.
    name = input("Enter name here: ").lower()
    #all the possible outcomes are set in the list expect "john"
    if name != "john" :
        newlist.append(name)
#list of all inputs are printed.
print("These are the names you have enetered: " , "\n" , newlist)



    
    
    
