time_given = int(input("Enter the number of seconds you want to convert: "))

minutes = time_given // 60
seconds = minutes % 60

print("The conversion is ", minutes, " minutes", seconds, "seconds")