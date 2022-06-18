#define modules here 


# define global varibales here 

# define functions here 

# define user-defined data-types here 
class Hotel :
    """@Hotel class <user-type> contains the order details,menu of hotel """
    item             = int(0)   
    totalPrice       = int(0)

    def printMenu(self):
        while self.item != int(99): 
             print(''' 
        +-------------------------------+
        |           Jain Hotel          |
        +-------------------------------+
        |[ITEMS]                [Prices]|
        +-------------------------------+
        |[1] Samosa                 25/-|
        +-------------------------------+
        |[2] Idli                   25/-|
        +-------------------------------+
        |[3] Dosa                   40/-|
        +-------------------------------+
        |[4] Sambar Wada            40/-|
        +-------------------------------+
        |[99] Place Order and Exit       |
        +-------------------------------+ ''')

             self.item = int(input("[+]Enter the key to order food item : "))
             if self.item == int(1) :
               self. totalPrice += int(25)
       
             elif self.item == int(2) :
                self.totalPrice += int(25)
       
             elif self.item == int(3) :
                 self.totalPrice += int(40)
      
             elif self.item == int(4):
                self. totalPrice += int(40)
      
             else :
                 print("Invalid choice")

                
# write main code here 
Customer = Hotel()
Customer.printMenu()
