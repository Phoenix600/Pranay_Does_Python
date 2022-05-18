# Import modules here 

# Define variables  or objects here 

items_sold_list = [157,2096,3054,197,25,0.5,8000,2000,5000]

'''Solution of 1) sub-problem statement '''
print(f"Total Selling prices todays     : {sum(items_sold_list)}")


'''Solution of 2) sub-problem statement '''
print(f"Highest cost items sold today   : {max(items_sold_list)}")

'''Solution of 3) sub-problem statement '''
print(f"Lowest cost items sold today    : {min(items_sold_list)} ")

'''Solution of 4) sub-problem statement '''
items_sold_list.sort()
print(f"Selling prices [MIN] to [MAX]   : {items_sold_list}")
