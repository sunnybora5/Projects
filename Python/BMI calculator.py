#User enter data for calculation of BMI.
weight = float (input("Enter your weight in kg here ?"))

height = float (input("Enter your height in meters ?"))

#BMI formula for calculation total BMI of user.
BMI = ((weight)/(height*height))

#IF statements for finding whether they are obese, overweight, normal or underweight.
if BMI >= 30:
                print ( "\nYour BMI states that you are obese")
                
elif BMI >= 25:
                print ("\nYour BMI states that you are overweight")
                
elif BMI >= 18.5:
                print ("\nYour BMI states that you are normal")
                
elif BMI < 18.5:
                print ("\nYour BMI staes thta you are underweight")
                

                
