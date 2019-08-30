
print ("\t\t\t\tParcel delivery")

print ("Here are the prices:")

print ('''Air R0.36 per Km or freight R0.25 per Km.\nFull insurance R50 or limited insurance R25.\nGift R15.00 or no gift R0.00.\nPriority R100 or standard delivery R20. ''')
         


#User enter data.
distance = float (input ("\nWhat is the distance your your parcel is travelling (in Km): "))

check_air = input ("How do you want you goods to be delivered? (Air or Freight)? ")

check_insurance = input ("what type of insurance would like to cover your parcel? (Full or Limited)? " )

check_gift = input ("Would you like a gift with your parcel? (Yes or No)? ")

check_delivery = input ("What type of delivery would you like your parcel? (Priority or Standard)? ")

# Data declared to a variable or number by means of if statements.
#delivery type.
if check_air == "Air":
        air = 0.36
        
elif check_air == "Freight":
        air = 0.25
#insurance        
if check_insurance == "Full":
        insurance = 50
        
elif check_insurance == "Limited":
        insurance = 25
#gift or no gift.        
if check_gift == "Yes":
        gift = 15
        
elif check_gift == "No":
        gift = 0
#delivery urgency.       
if check_delivery == "Priority":
        delivery = 100
        
elif check_delivery == "Standard":
        delivery = 20
        
# calculation of total delivery
final_amount = (distance*air) + insurance + gift + delivery

print ("\nYour total cost for the for sending your parcel is R" + str(final_amount))
