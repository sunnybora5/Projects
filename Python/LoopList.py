#This program prints out all my favourtite movies from a list.
#list stores my favourite movies
movies = ["Break fast club", "Ender's Game","Dope","Split","Sing Street"]
#numbering for the movies
no = 0
#Prints the movies in postion format.
print("These are my favourite movies \n")
for (num,movie) in enumerate(movies):
    no += 1
    print(str(no)+"."+movie)
