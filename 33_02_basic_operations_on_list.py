# Import modules here 

# Global variables 
int_sum = int(0)

list_sold_item_prices = [175,283,297,395,427,53]
for INDEX in range(0,len(list_sold_item_prices)) :
    int_sum = int_sum + int(list_sold_item_prices[INDEX])

print(f"items Sold today prices : {list_sold_item_prices}")
print(f"the total item sold prices : {int_sum}")

