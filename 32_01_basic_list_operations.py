# import yout modules here 

list_sample = [1,2,3,4,5,6,7,8,9,10]
list_odd_num = []
list_even_num = []

# index -1 , indicates the last item in sequence data type such as lists, strings & tuple
print("list_sample[-1] : ",list_sample[-1])

# Fifth item in Lists is <Item-5> =  5-1 = 4th Index , since index starts from 0 to N-1 , where N-1 is last Item in list 
print("list_sample[4] : ",list_sample[4])

for INDEX in range(0,len(list_sample)) :
    if list_sample[INDEX]%2 == 0:
        list_even_num.append(list_sample[INDEX])
    else :
        list_odd_num.append(list_sample[INDEX])

print("The given number list is : ",list_sample)
print("Even numbers : ",list_even_num)
print("Odd numbers  : ",list_odd_num)
