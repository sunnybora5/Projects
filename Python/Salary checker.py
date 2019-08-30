
print("\n")

print ("\t\tWelcome to the department store salary confirmation")


job_title = input ("\nDo you work as a Salesperson or Manager? (Salesperson or Manager) ")
if job_title == "Manager" or "manager" or "Manager":
    hours = int(input("\nHow many hours have you worked in the month? "))
    
#This is the code to calculate the how much the Manager's earns per month (hourly rate multiplied by the hours).
    amount_Manager = (40*hours)
    print ("\nThis is your monthly wage " + str(amount_Manager))
    
    
elif job_title == "Salesperson" or "salesperson" or "SALESPERSON"  :
    sales = int(input("\nWhat is your gross sales for the month? "))
    
#This is the code to calculate the how much the sales person earns per month (the 8% of tyhe commision plus the fixed moonthly wage).
    amount_Salesperson = (((8/100)*sales) + 2000)
    print ("\nThis is your monthly wage " + str(amount_Salesperson))
