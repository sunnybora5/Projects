#function that calculates total cost of hotel, car rental and plane ticket
#Takes the number of nights as an argument and return the total cost of the hotel stay
def hotel_cost(x):
    cost = x * 1020
    return cost
#Takes the city as an argument, then returns the cost of the plane trip
def plane_cost(city):
    if city == "Johannesburg":
        #price for ticket to johannesburg
        airplane_price = 2020
        #price for ticket to prt elizabeth
    elif city == "Port Elizabeth":
        airplane_price = 4090
        #price for a ticket to  anywhere
    else:
        airplane_price = 6823
    return airplane_price
#Takes the total number of days you will be renting a car, and returns the total value
def car_rental(days):
    tot_days = days * 250
    return tot_days
#Uses all three functions and returns the total cost of the holiday
def holiday_cost():
    night = int(input("How many nights will you be staying for?"))
    x_city = input("Which city will you be travelling to?")
    car_renting = int(input("For how many days do you want to rent a car for?"))
    # Calls the three functions and adds the totals
    total_cost = hotel_cost(night) + plane_cost(x_city) + car_rental(car_renting)
    print("The total cost of your holiday is: R" + str(total_cost))

holiday_cost()
