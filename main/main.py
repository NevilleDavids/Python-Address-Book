from Address import AddressOBJ, pd
filepath = "C:/Users/E1002734/Desktop/Python Assessment Project/addresses.csv"
myaddresses = AddressOBJ.LoadAddresses(filepath)
print(myaddresses)
newaddress = {}
def SearchAddress(Addresses):  #This method searches for entries matching the search term
    df = pd.DataFrame.from_dict(Addresses)
    sTerm = input("Search by street name: ")
    return df[(df["Street Name"].str.contains(sTerm))] #performs a regex search to find matching values
        

def AddressInput():
    StreetNo = int(input("Street No: "))
    StreetName = input("Street Name: ")
    Surburb = input("Surburb: ")
    Province = input("Province: ")
    AnAddress = AddressOBJ(StreetNo, StreetName, Surburb, Province)
    return AnAddress

def AddOrNot():     #used as switcher in the main method to determine whether to exit main method and to switch into different functions
    Ans  = input("Would you like to add an address (Y or N): ").capitalize()
    if Ans == "Y":
        newaddress = AddressInput() 
        newaddress.AddAddress(myaddresses)
        newaddress.WriteToCSV(filepath, myaddresses)
    if Ans == "N":
        #sTerm = input("Search by name: ")
        print(SearchAddress(myaddresses))

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
