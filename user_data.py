# Creating a wlecome page
print("Welcome User: ")

# Opening a file with details in there of each user
f = open("users.txt", "a")
header = "First Name, Last Name, E-mail, Password\n"
f.write(header)



#Details taken from user
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
mail = input("Enter E-mail Address: ")
passw = input("Enter Password: ")

#Printing results for user screen
print("\r\n First Name:  "+first_name+"\r\n")
print("\r\n Last Name:  "+last_name+"\r\n")
print("\r\n E-mail:  "+mail+"\r\n")
print("\r\n Password:  "+passw+"\r\n")


#Appending data to text file creatied individually
f.write("\r\n First Name:  "+first_name+"\r\n")
f.write("\r\n Last Name:  "+last_name+"\r\n")
f.write("\r\n E-mail:  "+mail+"\r\n")
f.write("\r\n Password:  "+passw+"\r\n")

f.close() # closing file with the required data
