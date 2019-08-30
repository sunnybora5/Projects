
#This program checks for if a number is a prime number.
#User inputs integer.
num = int(input("Enter any number above 1: "))

# checks if user number is greater than 1:
if num > 1:
    #The range of numbers that will be divide in to find the factors to determine if number entered by user is a prime number.
    for i in range (2,num):
        #This code divides numbers and determines if they not prime numbers.
        if (num%i) == 0:
         print( num ," is not a prime  number")
         break

    #If the number is a prime number this prints out.
        else:
            print(num, " is a prime number")
            break
#This prints out when the number is below or equal to 1.
elif num <= 1:
    print("This is not a prime number")
