# Import all your modules here 
'''Well in this case we don't have any modules to use them'''


# defining global variables 
string_message = ""

# function definations 

def getData() :
    
    # Acessing global variables using the global keyword
    global string_message

    string_message = input("(+)Enter the message  : ")


def solution() :
    
    # local variables 
    COUNT = int(0)
    REPEAT = int(0)

    ''' Solution A '''
    # Counting the number of characters in string message 
    for letter in string_message :
        COUNT = COUNT + 1

    print(f"No. of Charaters : {COUNT}")
    
    '''Solution B'''
    REPEAT = int(input("(+)Enter how many times you want to repeat the Message : "))
    print(string_message*REPEAT)
    
    
    '''Solution of C '''
    print(f"First charcter of message[0] :{string_message[0]}")

    '''Solution of D '''
    print(f"First 3 characters of message[0:4] : {string_message[0:3]}")

    ''' Solution of F '''
    print(f"Last 3 charcters of message[-3: ] : {string_message[-3:]}")

    ''' Solution of G '''
    print(f"Message in Reverse : {string_message[::-1]}")

    ''' Solution of H '''
    ''' Printing the seventh character of string '''
    if len(string_message) >= 7 :
        print(f"{string_message[6]} is the seventh charcater in string.")
    else :
        print("Inserted string is not long enough :( ")



    '''Solution of I  '''

    # assigning string_message to string_message_02 
    string_message_02 = string_message[1 :int(len(string_message)-1)] 
    print(string_message_02)

    ''' Solution of J '''
    
    # temprary string to convert all lowercase char into upper case
    string_upper_case = ""

    for INDEX in range(0,len(string_message)) :
        
    # if there is space, if block code will add space 
        if string_message[INDEX] == " " :
            string_upper_case = string_upper_case + " "+ chr(ord(string_message[INDEX])-32) 

    # by subtracting the asci value 32 , we can convert the lowercase charcater into Uppercase
        else:
            string_upper_case = string_upper_case + chr(ord(string_message[INDEX])-32) 


    print("String in upper case : " + string_upper_case)
    
    ''' Solution of K'''
    string_replaced = ""

    for INDEX in range(0,len(string_message)) :
        #print(string_message[INDEX])
        if string_message[INDEX] == 'a' or string_message[INDEX] =="a":
            string_replaced =  string_replaced[0:INDEX]+ "e" + string_replaced[INDEX+1:]
        else :
            string_replaced = string_replaced + string_message[INDEX] 

    print(string_replaced)

# Driver code
getData()
solution()
