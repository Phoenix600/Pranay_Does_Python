# import all your modules here 

# Intially keeping strings as empty strings 
string_01 = ""
string_02 = ""
bool_flag = True   # By default empty string is a palindrome stirng, if empty string is passed as parameter or accessed globally
# function defination will be defined here 

def isPalindrome() :
    '''@isPalindrome() function to check wheather the string is palindrome or not, this function will 
    return the < bool-class > object it will be either True or False
    '''
    global string_1
    global string_2 
    global bool_flag

    string_1 = input("[+]Enter the string to check wheather it is palindrome or not : ")
    int_SIZE = int(len(string_1))
    string_2 = string_1

    for INDEX in range(0,int(len(string_1)/2)):
        if string_1[INDEX] == string_2[int(len(string_1) - INDEX-1)] :
            pass
        else :
            bool_flag = False


isPalindrome()
print("Palindrome : [Status] [True/False] : ",bool_flag)

