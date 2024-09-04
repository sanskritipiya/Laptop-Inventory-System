

def laptop_dictionary():
    laptop_dt = {}
    file_f=open("Laptop.txt" ,"r")
    laptop_id=1
    for line in file_f:
        line=line.replace("\n","")
        laptop_dt.update({laptop_id : line.split(",")})
        laptop_id=laptop_id+1
    file_f.close()
    return laptop_dt



def laptop_print():
    
    main_information = laptop_dictionary()
    print("-------------------------------------------------------------------------------------------")
    print("S.N\tLaptop Name\tCompany Name\tPrice\tQuantity\t Processor\t Graphic Card")
    print("-------------------------------------------------------------------------------------------")
    file = open("Laptop.txt","r")
    sn = 1
    for line in file:
        print(sn,"\t",line.replace(",","\t"))
        sn += 1
    file.close() 
        
