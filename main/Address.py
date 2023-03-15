import pandas as pd
class AddressOBJ():
    def __init__(self,streetno, streetname, suburb, province):
        self.streetno = streetno
        self.streetname = streetname
        self.suburb = suburb
        self.province = province

    def LoadAddresses(filepath):
        """This method takes a CSV of addresses and returns a list of dictionaries"""
        df = pd.read_csv(filepath)
        Addresses = df.to_dict("records")
        return Addresses
    def AddAddress(self, Addresses):
        """This method allows us to add a new address to an existing address dicitionary list"""
        NewAddress = {"Street no": self.streetno, "Street Name": self.streetname, "Surburb":self.suburb, "Province": self.province}
        Addresses.append(NewAddress)

    def WriteToCSV(self, filepath , ListOfAddresses):
        """This method allows for writing to a new csv once all changes have been made to the address book"""
        df = pd.DataFrame.from_dict(ListOfAddresses)
        df.to_csv(filepath, encoding ='utf-8', index = False)