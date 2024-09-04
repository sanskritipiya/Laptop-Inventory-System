import operation
print("\n")
print("\n")
print("\t\t\t\t\t\t SANSKRITI APPLIANCE")
print("\n")
print("\t\t\t\t\tHattiban, Lalitpur, Nepal| Phone No:9825254001")
print("\n")
print("\t \t \t \t Warm Welcome to the system!Hope you have a Virtuos Day!")
print("\n")
def main():
    # Sets the loop to enter the while loop program
    loop = True
    while loop==True:
        try:
            decision = input("\n \n\
                             Please select one of the following options:\
                             \nPress M to purchase a laptop.\
                             \nPress N to sell a laptop.\
                             \nPress O to exit the program.\
                             \nPlease enter your choice: ").upper()
            loop = False
        except:
            print("The given input is not valid")

        if decision == "M":
            operation.purchase_from_manufacture()
            loop = True
        elif decision == "N":
            operation.Selling_to_customer()
            loop = True
        elif decision == "O":
        
            exit_choice = input("Are you sure you want to exit the program? (Yes/No): ")
            if exit_choice == "Yes":
                print("\n---------------------------------------------------------------------")
                print("Thank you for shopping with us. Hope you enjoyed it. Please visit again!")
                print("---------------------------------------------------------------------\n")
                loop = False
        else:
            print("---------------------------------------------------------------------")
            print("Please select one of the provided options.")
            print("---------------------------------------------------------------------")
            loop = True


main()
