# import your modules here 


# write your code here 

# define variables here 
SUM = int(0)

# Defination & declartion of Lists 
list_numbers = [1,2,3,4,5,6,7,8,9]

# Caculating the sum of list elements using predefined or built-in-function 
print("sum(list_number) : ",sum(list_numbers))


# Caculating the sum of list elements/ ITEMS using for loop 
for INDEX in range(0,len(list_numbers)) :
    SUM += list_numbers[INDEX]

print(f"Sum using for loop : {SUM}")
