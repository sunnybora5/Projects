product1 = input ("Enter name of product 1: ")
product1_price = float (input("Enter price for product 1: R"))


product2 = input ("\n""Enter name of product 2: ")
product2_price = float (input("Enter price for product 2 R"))

print("\n")
product3 = input ("Enter name of product 3: ")
product3_price = float (input("Enter price of product 3: R"))


#This code rounds the ouput so thats can easily read it.      
sumofall = product1_price+product2_price+product3_price
ave_price = sumofall/3
      

#This code rounds the ouput so thats can easily read it.     
smround = round(sumofall,3)
ave_round = round(ave_price,3)
      
print("\n")
      
print ("The Total of " + product1 + "," + product2 + "," + product3 + " is " "R"+ str(smround)
       + " and the average price of the items are " + "R" + str(ave_round))
