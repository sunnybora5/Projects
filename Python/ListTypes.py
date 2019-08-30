#Empty list which will be containing names of tghe users.
friends_names = list()
#Empty list which will be containing ages of the users.
friends_ages = list()
#Repeats the process of adding the content to lists and asking the user to eneter their agaes and names.
for i in range (1,4):
    #user inputs their name
    friendsNames = input("Enter your full name here: ")
    #User inputs their age.
    friendsAges = input("Enter your age here: ")
    #User names are stored in a list.
    friends_names.append(friendsNames)
    #user age is stored in a list.
    friends_ages.append(friendsAges)
    
    
print(friends_names[0]+" "+friends_ages[0]+"\n"+friends_names[2]+" "+friends_ages[2])



