# import yout modules here

''' split() is method is which is member function of seqence classes such as list, string,tuple, dictonaries and etc 
    When used with strtings it splits the the whole string into list which contains group of words and not characters
    onece its is converted into list perform all desired operation on the data and then convert it into string by join
    funciton  <'JOINER'>join(arg** string) funciton 

'''

string_sample = input("[+]Enter the message : ")
string_to_list_split = string_sample.split()

for INDEX in range(0,len(string_to_list_split)) : 
    if string_to_list_split[INDEX]  == "Nagpur" or string_to_list_split[INDEX] == "nagpur" :
        string_to_list_split[INDEX] = "Pune"
    else :
        pass

string_new = ' '.join(string_to_list_split)
print(string_to_list_split)
print(string_new)

