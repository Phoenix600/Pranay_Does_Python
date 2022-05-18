# Declare your global variables here 
string_first_name = ""
string_last_name  = ""
string_user_name  = ""
string_DOB = ""
string_passwd = ""

def createAccountName():

    #Accessing variable as global 
    global string_first_name 
    global string_last_name
    global string_user_name
    global string_DOB
    global string_passwd

    # Generating @username : 
    print("Enter the following details to create account username : ")
    string_first_name = input("(+)Enter your first name : ")
    string_last_name  = input("(+)Enter your last name  : ")
    
    # If passed string is in uppercase convert it to lowercase using @lower() method
    string_first_name = string_first_name.lower()
    string_last_name  = string_last_name.lower()

    # creating the user name as first three char from Fname and Lname 
    string_user_name = string_first_name[0:4]+"_" + string_last_name[0:4]
  
    # Creating password for user
    string_DOB = input("[+]Enter your date of birth : DD/MM/YYYY : ")
    string_passwd = string_first_name[0:4] + "@" + string_DOB
    print(f"[BANK]> User name and passwd has been created successfully")
    print('''
    +-----------------------------------+
    |       BANK OF MAHARASHTRA         |
    +-----------------------------------+
    |   Username       |    Password    |
    +-----------------------------------+
    | {0}        | {1}  |
    +-----------------------------------+
            '''.format(string_user_name,string_passwd))
   
    string_passwd = input("[BANK OF MAHARASHTRA] > Change default password into more secure password : ")
    print("[OK] : Password updated successfully")

# main code starts here 

createAccountName()
