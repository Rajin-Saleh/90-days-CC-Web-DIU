# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("P")

#result = name.rfind("P")

# result = name.capitalize()

# name = name.upper()
# name = name.lower()

# result = name.isdigit()
# result = name.isdigit()
# result = name.isalpha()


# number = input("Enter you phone number: ")

# result = number.replace("-", "")



#print(help(str))




# print(result)




username = input("Enter a username: ")

username.find(" ")


if len(username) > 12:
    print("Your user name can't be more than 12 char")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.")    
elif not username.isalpha():
    print("Your username can't contain numbers.")
else:
    print(f"Welcome {username}")    

































