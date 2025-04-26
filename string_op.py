x = input("Enter a string:\n")
len = int(len(x))
if len <= 3:
    print("The string is too short to operate")
    exit()
elif len > 3 and len <= 10:  
    print("The length of the string is: " + str(len))
    ips = x[0:1]
    print("The word is starting with letter: " + ips)
else:
    print ("The length of the string is: " + str(len) + "\nThe string is too long to operate")
    exit()