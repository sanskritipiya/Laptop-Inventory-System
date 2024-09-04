import datetime

    
def update(laptop_dt):
    file_ = open("Laptop.txt", "w")
    for values in laptop_dt.values():
        file_.write(str(values[0]) + ", " + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]) + "\n")
    return laptop_dt

def invoice_Customer(purchased_items, Cost_of_shipping):
    date_time = datetime.datetime.now()
    _maintotal = 0
    total = 0
    #for billing
    print("\n")
    print("For bill please enter the following details ")
    print("\n")
    Name = input("Enter the name: ")
    print("\n")
    Contact_Number = int(input("Enter the phone number: "))
    print("\n")
    Address_of_Customer = input("Enter the Customer's Address : ")
    print("\t \t \t \t \t Bill of the Laptop")
    print("\n")
    print("\t \t \t \t SANSKRITI APPLIANCE")
    print("\n")
    print("\t \t \t Hattiban, Lalitpur | Phone No: 9825254001")
    print("\n")
    print("----------------------------")
    print("The Details of Laptop are:")
    print("----------------------------")
    print("Name of the customer:", Name)
    print("\n")
    print("Contact number:", Contact_Number)
    print("\n")
    print("Address : ", Address_of_Customer)
    print("\n")
    print("Date and time of purchase:", date_time)
    print("\n")
    print("-----------------------------------------------------------")
    print("Laptop Name\t\tQuantity\t\tPrice\t\tTotal")
    print("-----------------------------------------------------------")
    for i in purchased_items:
        print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t$", i[3])
        total += i[3]
    _maintotal = total + Cost_of_shipping
    print("\n \n")
    print("Total amount: " , total)
    print("\n")
    print("Shipping cost is:", Cost_of_shipping)
    print("\n")
    print("Grand total: $", _maintotal)
    print("\n")
    
    #for invoice
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    minute = str(datetime.datetime.now().minute) 
    hour = str(datetime.datetime.now().hour)
    second = str(datetime.datetime.now().second)
    name = Name+ str(Contact_Number)+ year+month+ day + minute + hour + second
    
    file = open(str(name)+ ".txt", "w")
    file.write("\n")
    file.write("\t\t\t\t Details of the bill")
    file.write("\n")
    file.write("\t\t\t  SANSKRITI APPLIANCE")
    file.write("\n")
    file.write("\t \t Hattiban, Lalitpur| Phone No:9825254001")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("The details of the Laptop are:")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Name_of_the_customer: " + str(Name) + "\n")  
    file.write("\n")
    file.write("Contact_number: " + str(Contact_Number) + "\n") 
    Total_Price = 0
    file.write("   --------------------------------------------")
    file.write("\n")
    file.write("Details of the purchase made:")
    file.write("\n")
    file.write("   ---------------------------------------------")
    file.write("\n")
    file.write("Laptop Name\t\tQuantity\tPrice\tTotal")
    file.write("\n")
    file.write("------------------------------------------------")
    file.write("\n")
    for i in purchased_items:  
        file.write(i[0] + "\t " + str(i[1]) + "\t\t" + str(i[2]) + "\t\t" + "$" + str(i[3]))
        file.write("\n")
        Total_Price += int(i[3])
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------")
    file.write("Total amount: " + str(total))
    file.write("\n")
    file.write("Shipping cost is: " + str(Cost_of_shipping))  # Added string conversion
    file.write("\n")
    file.write("Grand Total: $" + str(_maintotal))  # Added string conversion
    file.write("\n")
    file.write("Shipping cost is added to the main total" + "\n")
    file.write("\n")
    
    file.close()  # Added parentheses to close the file



def invoice_manufacture(purchased_items):
    date_time = datetime.datetime.now()
    _maintotal = 0
    total = 0
    #for billing
    print("\n\n")
    Name = input("Enter the name of the Company: ")
    print("\n")
    Contact_Number = int(input("Enter the phone number: "))
    print("\n")
    Address_of_Company = input("Enter the address of the company : ")
    print("\n")
    print("\t\t\t\t\tBill of Laptop Shop")
    print("\n")
    print("\t \t \tSANSKRITI APPLIANCE")
    print("\n")
    print("\t\t\tHattiban, Lalitpur | Phone No: 9825254001")
    print("\n")
    print("----------------------------------")
    print("The Details of Laptop are:")
    print("----------------------------------")
    print("Name of the customer:", Name)
    print("\n")
    print("Contact number:", Contact_Number)
    print("\n")
    print("Address : ",Address_of_Company)
    print("Date and time of purchase:", date_time)
    print("\n")
    print("----------------------------------------------------------------")
    print("Laptop Name\t\tQuantity\t\tPrice\t\tTotal")
    print("----------------------------------------------------------------")
    for i in purchased_items:
        print(i[0], "\t\t", i[1], "\t\t", i[2], "\t\t$", i[3])
        total += i[3]
    vat = total*(13/100)
    _maintotal = vat + total
    print("\n")
    print("Total amount: " , total)
    print("\n")
    print("Vat amount:", vat)
    print("\n")
    print("Grand total: $", _maintotal)
    print("\n")
    
    #for invoice
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    minute = str(datetime.datetime.now().minute) 
    hour = str(datetime.datetime.now().hour)
    second = str(datetime.datetime.now().second)
    name = Name+ str(Contact_Number)+ year+month+ day + minute + hour + second
    
    file = open(str(name)+ ".txt", "w")
    file.write("\n")
    file.write("\t \t \t \t Details of the bill")
    file.write("\n")
    file.write("\t \t \t \t SANSKRITI APPLIANCE")
    file.write("\n")
    file.write("\t \t \t Hattiban, Lalitpur| Phone No:9825254001")
    file.write("\n")
    file.write("----------------------------------------------------------------")
    file.write("\n")
    file.write("The Details of the Laptop are:")
    file.write("\n")
    file.write("----------------------------------------------------------------")
    file.write("\n")
    file.write("Name of the Company: " + str(Name) + "\n")  
    file.write("\n")
    file.write("Contact_number: " + str(Contact_Number) + "\n")
    file.write("\n")
    Total_Price = 0
    file.write("     ----------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t \tDetails of the purchase made:")
    file.write("\n")
    file.write("     -----------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Laptop Name\tQuantity\tPrice\t\tTotal")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    for i in purchased_items:  
        file.write(i[0] + "\t " + str(i[1]) + "\t" + str(i[2]) + "\t" + "$" + str(i[3]))
        file.write("\n")
        Total_Price += int(i[3])
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Total amount: " + str(total))
    file.write("\n")
    file.write("Vat amount: " + str(vat))  # Added string conversion
    file.write("\n")
    file.write("Grand Total: $" + str(_maintotal))  # Added string conversion
    file.write("\n")
    file.write("Shipping cost is added to the main total" + "\n")
    file.write("\n")
    file.close()  # Added parentheses to close the file
