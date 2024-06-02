import settings
import datetime
import pandas as pd

class Database:
    def __init__(self):
        pass

    def getInventory(self):
        return pd.read_csv(settings.pathToInventory)

    def getInventoryList(self):
        return pd.read_csv(settings.pathToInventoryList)    
    def getList(self):
        return pd.read_csv(settings.pathToPersonalList)

    #functions to save different inventorys
    def saveInventory(self,df):
        df.to_csv(settings.pathToInventory, index=False)
    
    def saveInventoryList(self,df):
        df.to_csv(settings.pathToInventoryList, index=False)

    def savePersonalList(self,df):
        df.to_csv(settings.pathToPersonalList, index=False)

    def saveShoppingList(self,df):
        df.to_csv(settings.pathToShoppingList, index=False)

    # adds new item to inventory inventory
    def addItem(self, name): #returns string
            
        df = self.getInventory()
        print(df)

        try:
            if(not df.isin([name.lower()]).any().any()):
                df = df._append({'Name':name.lower(),'amount':0}, ignore_index=True)
                
                self.saveInventory(df)
                #df.to_csv(settings.pathToInventory, index=False)

                return True
            else:
                raise ValueError(f"{name.lower()} already exists in inventory, nothing added")
        
        except Exception as e:
            print(e)
            return False
    

    # removes item from inventory
    def removeItem(self, name): #returns string
        
        df = self.getInventory()

        try:

            if(name.lower() in df["Name"].values):
                
                df = df[df['Name'] != name.lower()]
                
                self.saveInventory(df)
                #df.to_csv(settings.pathToInventory,index=False)
                return True
            else:
                raise ValueError(f"{name.lower()} does not exist in inventory, nothing removed")
        except Exception as e:
            print(e)
            return False
    
    # reduces inventory quantity by amount
    def justAte(self, name, amount):
        amount = int(amount)

        df = self.getInventory()
        try:
            if name.lower() in df["Name"].values:
                
                df.loc[df['Name'] == name.lower(), 'amount'] -= amount
                
                df['amount'] = df['amount'].clip(lower=0)
                
                self.saveInventory(df)
                
                return True
            else:
                raise ValueError(f"{name} not in inventory, nothing changed")
            
        except Exception as e:
            print(e)
            return False
    
    # increases inventory quantity by amount
    def setInventoryQuantity(self, name, amount):
        amount = int(amount)
        df = self.getInventory()

        try:

            if name.lower() in df["Name"].values:
                
                df.loc[df['Name'] == name.lower(), 'amount'] = amount
                self.saveInventory(df)
                
                return True
            else:
                raise ValueError(f"{name} not in inventory, nothing changed")
            
        except Exception as e:
            print(e)
            return False

    """
    #adds item to PERSONAL shopping list
    def addToList(self,name):
        df = self.getList()
        try:
            if(not name.lower() in df["Name"].values):
                df = df._append({'Name':name.lower(),'amount':1}, ignore_index=True)

                self.saveList(df)

                return True
            else:
                raise ValueError(f"{name.lower()} already exists on list, nothing added")
        
        except Exception as e:
            print(e)
            return False
    
    #removes item from PERSONAL shopping list
    def removeFromList(self,name):
        df = self.getList()

        try:

            if(name.lower() in df["Name"].values):
                
                df = df[df['Name'] != name.lower()]
                
                self.saveList(df)
                return f"{name.lower()} removed from list"
            else:
                raise ValueError(f"{name.lower()} does not exist in list, nothing removed")
        except Exception as e:
            print(e)
    """

    def goShopping(self, _):
        inventoryDF     = self.getInventory()
        inventoryListDF = self.getInventoryList()

        zeroQtyItems = inventoryDF[inventoryDF['amount']<=0]


        inventoryListDF = pd.concat([inventoryListDF,zeroQtyItems], ignore_index=True)

        self.saveInventoryList(inventoryListDF)
        # somehow print this: inventoryListDF
        print(inventoryListDF)


        return True# if it worked



    def wentShopping(self, total):
        pass



    def ranOut(self, name):
        pass
        #sets amount to 0
