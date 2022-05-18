# import all your modules here 


# write your code here 

''' Getting statred with lists '''

'''
    ---------------------------------------------------------------------------------------------------------------------------
    [LISTS] : 
    ---------------------------------------------------------------------------------------------------------------------------
    * What is list 
        List is an linear-data-structure where different or similar type of data is stored squentially under a single name  
        and acceses via indexing 
    ---------------------------------------------------------------------------------------------------------------------------
    * How to create Lists ?
        list can be created by namin_list object followed by the '[ ]' square brackets, where each item in [item1,item2,.... ] 
        is seprated by ',' comma
        Ex. 
        fav_dishes = ["Idli","Dosa","Sambar Vada"] ------> List of similar data 
        player = ["Pranay","12/12/2012",19,"Single",80.6]

    ----------------------------------------------------------------------------------------------------------------------------
    * 
'''


friends_list = ['Vedant F','Vishal P','Anurag S','Devreshi T','Mayur D','Appu H']
print(friends_list)

for friend in friends_list :
    print(f"{friend} is my best friend")
    break


random_list = [1,2,3,4,5,"ravan",12.12,17.05,13.13,"A",'c','B',"sita"]

print(random_list)
print(list(range(0,len(random_list))))
print(random_list[1 :(len(random_list)-4 ): 2])



