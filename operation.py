import datetime
import read
import write

#Checking the Id that has been inputed by the user  
def id_validation():
    file_=open("Laptop.txt", "r")
    laptop_dt = read.laptop_dictionary()
    

    while True:
        try:
            validation = int(input("Enter the product ID of the Laptop you want: "))
            print("\n")

            while validation <= 0 or validation>(5):
                print("The input you have entered is invalid. Please enter a valid ID of the laptop.")
                print("\n")
                validation = int(input("Enter the valid product ID of the product: "))
                print("\n")

            return validation
        except:
            print("The input you have entered is not valid. Please enter a valid input.")
            print("\n")
            continue


def quantity_(quantity_id):
    laptop_dt = read.laptop_dictionary()
    Selection_of_laptop_quantity = int(laptop_dt[quantity_id][3])

    while True:
        try:
            selection_of_quantity_by_user = int(input("Please specify the number of laptops: "))
            print("\n")
            

            while selection_of_quantity_by_user <= 0 or selection_of_quantity_by_user > Selection_of_laptop_quantity:
                print("The quantity you just provided is either invalid or not enough.")

            return selection_of_quantity_by_user
        except:
            print("The input you have entered is not valid. Please enter a valid input.")
            continue


def Selling_to_customer():
    purchased_items = [] #list to store the items purchased 
    answer = "YES"
    while answer == "YES":
        laptop_dt = read.laptop_dictionary()
        read.laptop_print()
        
        validation = id_validation()
        quantityofuser = int(quantity_(validation))
        laptop_dt[validation][3] = int(laptop_dt[validation][3]) - quantityofuser
        write.update(laptop_dt)
        product_name = laptop_dt[validation][0]
        selection_ofquantity_by_user = quantityofuser
        price = laptop_dt[validation][2]
        Selected_item_price = laptop_dt[validation][2].replace("$", "")
        Main_Price = int(Selected_item_price) * int(selection_ofquantity_by_user)

        Laptop_purchased_by_the_user = []
        
        Laptop_purchased_by_the_user.append(product_name)
        Laptop_purchased_by_the_user.append(selection_ofquantity_by_user)
        Laptop_purchased_by_the_user.append(price)
        Laptop_purchased_by_the_user.append(Main_Price)
        purchased_items.append(Laptop_purchased_by_the_user)
        answer = input("do you want to buy more items (yes/no) :").upper()
        if answer == "NO":
            shipping = input("Dear users, do you want your laptops to be shipped? (Yes or No): ").upper()
            print("\n")
            if shipping == "YES":
                Cost_of_shipping = 150
               
            else:
                Cost_of_shipping = 0
            write.invoice_Customer(purchased_items, Cost_of_shipping)
        else:
            answer = "YES"
            

def purchase_from_manufacture():
    purchased_items = [] #list to store the items purchased 
    answer = "YES"
    while answer == "YES":
        laptop_dt = read.laptop_dictionary()
        read.laptop_print()
        
        validation = id_validation()
        quantityofuser = int(input("Enter the quantity you want: "))
        laptop_dt[validation][3] = int(laptop_dt[validation][3]) + quantityofuser
        write.update(laptop_dt)
        product_name = laptop_dt[validation][0]
        selection_ofquantity_by_user = quantityofuser
        price = laptop_dt[validation][2]
        Selected_item_price = laptop_dt[validation][2].replace("$", "")
        Main_Price = int(Selected_item_price) * int(selection_ofquantity_by_user)

        Laptop_purchased_by_the_user = []
        
        Laptop_purchased_by_the_user.append(product_name)
        Laptop_purchased_by_the_user.append(selection_ofquantity_by_user)
        Laptop_purchased_by_the_user.append(price)
        Laptop_purchased_by_the_user.append(Main_Price)
        purchased_items.append(Laptop_purchased_by_the_user)
        answer = input("Do you want to buy more items (yes/no) :").upper()
        if answer == "NO":
            write.invoice_manufacture(purchased_items)
        else:
            answer = "YES"
            
                 
