from Address import AddressOBJ
filepath = "C:/Users/E1002734/Desktop/Python Assessment Project/addresses.csv"
myaddresses = AddressOBJ.LoadAddresses(filepath)
print(myaddresses)
newaddress = {}
def SearchAddress(Dictionary, term):  #This method searches for entries matching the search term
        return next((i for i in Dictionary if i["Street Name"] == term), None) 
 
def AddOrNot():     #used as switcher in the main method to determine whether to exit main method and to switch into different functions
    Ans  = input("Would you like to add an address (Y or N): ").capitalize()
    if Ans == "Y":
        StreetNo = int(input("Street No: "))
        StreetName = input("Street Name: ")
        Surburb = input("Surburb: ")
        Province = input("Province: ")
        newaddress = AddressOBJ(StreetNo, StreetName, Surburb, Province)
        newaddress.AddAddress(myaddresses)
        newaddress.WriteToCSV(filepath, myaddresses)
    if Ans == "N":
        sTerm = input("Search by name: ")
        print(SearchAddress(myaddresses, sTerm))

def main():
    while True:
        AddOrNot()
        Exit = input("Would you like to exit (Y / N): ").capitalize()
        if Exit == "N":
            pass
        elif Exit == 'Y':
            break
        else:
            print("Unknown input")

main()
quit()
