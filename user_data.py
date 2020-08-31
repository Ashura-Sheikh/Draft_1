from Question import Question


    # Creating a wlecome page
#    print("Welcome User: ")

    # Opening a file with details in there of each user
#    f = open("users.txt", "a")
#    header = "First Name, Last Name, E-mail, Password\n"
#    f.write(header)



    #Details taken from user
#    first_name = input("Enter First Name: ")
#    last_name = input("Enter Last Name: ")
#    mail = input("Enter E-mail Address: ")
#    passw = input("Enter Password: ")

    #Printing results for user screen
#    print("\r\n First Name:  "+first_name+"\r\n")
###    print("\r\n Password:  "+passw+"\r\n")


    #Appending data to text file creatied individually
#    f.write("\r\n First Name:  "+first_name+"\r\n")
#    f.write("\r\n Last Name:  "+last_name+"\r\n")
#    f.write("\r\n E-mail:  "+mail+"\r\n")
#    f.write("\r\n Password:  "+passw+"\r\n")

#    f.close() # closing file with the required data


print("Lets play a game of questionaire....")


# Questions Prompted
question_propmts = [

      "solve the problem, a=3, b=4. so a+b(b*a)=?\n (a)49\n, (b)14\n\n"

      "what does py relate to?\n (a)Problem-Yearning\n, (b)Py-charm\n\n"

      "I have water within me, yet i do not drown?\n, (a)Sea\n, (b)Human\n\n"

]
# Questions Answers
question = [

        Question(question_propmts[0], "a"),
        Question(question_propmts[1], "b"),
        Question(question_propmts[2], "b"),

]

# define what function would be played and how
def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got" + str(score) + "/" + str(question) + "Correct")


run_test(question)
