# for loop:
print("Print numbers using for loop are :")
for i in range(10):
    print(i)

# while loop:
print("Print numbers using while loop are :")
i=10
while (i<20):
    print(i)
    i+=1

# printing a triangle pattern of 4:
# 1   
# 1 2    
# 1 2 3     
# 1 2 3 4 
# num = int(input("Enter number to print pattern upto lines:"))
# for i in range(1,num+1):
#     print(i*" ")
#     for j in range(1,i+1):
#         print(j,end=" ")


# Python program that takes an integer input from the user and prints the sum of all even numbers from 1 to that number (inclusive).
# number = int(input("Enter number to get the sum of evens till the number(inclusive): "))
# sum=0
# for i in range(number):
#     if i%2 == 0:
#         sum+=i
# print(sum)

# Python program that takes an integer input from the user and calculates the factorial of that number using a while loop.
# try:
#     fact_num = int(input("Enter integer to calculate factorial of number: "))
#     fact_result = 1
#     if(fact_num < 0):
#         print("Invalid")
#     else:
#         while(fact_num > 1):
#             fact_result *= fact_num
#             fact_num -= 1
#         print(fact_result)
# except ValueError:
#     print("Invalid input! Enter valid number")

# Python program to help a store manager manage the inventory of items in the store. The program will:
# Problem Statement:
# Take a list of item names (space-separated) from the user.
# For each item, ask the user for the quantity in stock and the price per unit.
# Classify each item based on its stock level:
# If the stock is 0: Print "Out of stock"
# If the stock is less than 5: Print "Low stock"
# For stock greater than 5: Print "Stock Available"
# Otherwise, print "In stock"
# Calculate the total value of inventory for each item (quantity * price).
# Print a summary report showing the item name, stock classification, and the total value of the item in the inventory.


def add_item(inventory,item_name, item_price, item_qty):
    inventory[item_name] = {"Price" : item_price, "Qty" : item_qty, "HasStock" : "Low Stock" if (item_qty < 5 and item_qty > 0) else "Out of stock" if item_qty == 0 else "Stock Available"}

def display_inventory(inventory):
    print("\nItems in the inventory:")
    print("{0:15}{1:10}{2:15}{3:35}{4:10}".format("Item","Price","Quantity","Stock","Total Value(in Rs.)"))
    for item,details in inventory.items():
        print("{0:15}{1:<10}{2:<15}{3:<35}{4:<10}".format(item,details['Price'],details['Qty'],details['HasStock'],details['Qty']*details['Price']))

def show_options(inventory):
    showOptionsBool = True
    while(showOptionsBool):
        print("\nEnter numbers to perform operations:\n 1 - View Inventory \n 2 - Edit Inventory \n 3 - Remove Item from Inventory \n 4 - Add Item to Inventory \n 0 - Show Options \n Any Key - Exit")
        try:
            operation = int(input())
            if operation == 1:
                display_inventory(inventory)
            
            elif operation == 2:
                edit_item = input("Enter the item(full name) that you want to edit it's values: ")
                
                if edit_item in list(inventory.keys()):
                    print("\n Enter\n 1 - To edit the Price \n 2 - To edit the quantity \n 3 - To edit the name of the Item")
                    val = int(input())
                    if val == 1:
                        print(f"Current old Price of {edit_item} is {inventory[edit_item]['Price']}")
                        inventory[edit_item]['Price'] = int(input("Enter the new Price Value."))
                        print("Price changed successfully")
                        display_inventory(inventory)
                    elif val == 2:
                        print(f"Current old Quantity of {edit_item} is {inventory[edit_item]['Qty']}")
                        inventory[edit_item]['Qty'] = int(input("Enter the new Quantity Value."))
                        print("Quantity changed successfully")
                        display_inventory(inventory)
                    elif val == 3:
                        vals = inventory.pop(edit_item)
                        item_name = input("Enter the new name you wanted to give.")
                        inventory[item_name] = vals
                        print("Name changed successfully")
                        display_inventory(inventory)
                    else:
                        print("Entered invalid input\nOperation Failed")
                else:
                    print(f"No item available with name - {edit_item}\nOperation Failed")

            elif operation == 3:
                remove_item = input("Enter the item(full name) that you want to remove: ")
                if remove_item in list(inventory.keys()):
                    if len(list(inventory.items())) > 1:
                        inventory.pop(remove_item)
                        print(f"Removed {remove_item} from inventory")
                    else:
                        print("Cannot Empty the inventory.")
                    display_inventory(inventory)
                else:
                    print(f"No item available with name - {remove_item}\nOperation Failed")
            
            elif operation == 4:
                val = input(f"Enter item name to Inventory: ")
                price = int(input(f"Enter the price of item: "))
                qty = int(input(f"Enter how many qty of items you have: "))
                add_item(inventory,val,price,qty)
                display_inventory(inventory)
            
            else:
                print("Invalid Value entered.")
            
        except ValueError:
            showOptionsBool = False
            print("Thanks for Using our Inventory. Try our work Again")

exit = False
while(exit == False):
    try:
        print("Welcome to the \"INVENTORY MANAGEMENT\" \nYou have no items in the inventory as you are new.\nType negative number to exit.")
        item_num=int(input("\nEnter number of items you want to add to start with:"))
        if(item_num == 0):
            print("\nItems must be positive value(s) only")
        elif item_num > 0:
            items=[]
            inventory = {}
            for _ in range(item_num):
                val = input(f"Enter {_+1} item(s): ")
                price = int(input(f"Enter the price of {_+1} item(s): "))
                qty = int(input(f"Enter how many qty of {_+1}items you have: "))
                add_item(inventory,val,price,qty)
            show_options(inventory)
        else:
            exit = True
            print("It seems that you want to exit :(\nOk! Let/'s catch you up again. ")
        
    except ValueError:
        print("\nEnter Valid input!\nItems must be positive value(s) only")

