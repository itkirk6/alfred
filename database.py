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

                return f"{name.lower()} added with amount {0}"
            else:
                raise ValueError(f"{name.lower()} already exists in inventory, nothing added")
        
        except Exception as e:
            print(e)
    

    # removes item from inventory
    def removeItem(self, name): #returns string
        
        df = self.getInventory()

        try:

            if(name.lower() in df["Name"].values):
                
                df = df[df['Name'] != name.lower()]
                
                self.saveInventory(df)
                #df.to_csv(settings.pathToInventory,index=False)
                return f"{name.lower()} removed from inventory"
            else:
                raise ValueError(f"{name.lower()} does not exist in inventory, nothing removed")
        except Exception as e:
            print(e)
    
    # reduces inventory quantity by amount
    def justAte(self, name, amount):

        df = self.getInventory()
        try:
            if name.lower() in df["Name"].values:
                
                df.loc[df['Name'] == name.lower(), 'amount'] -= amount
                
                df['amount'] = df['amount'].clip(lower=0)
                
                self.saveInventory(df)
                
                return f"{name.lower()} reduced by {amount}"
            else:
                raise ValueError(f"{name} not in inventory, nothing changed")
            
        except Exception as e:
            print(e)
    
    # increases inventory quantity by amount
    def addInventoryQuantity(self,name, amount):
        df = self.getInventory()

        try:

            if name.lower() in df["Name"].values:
                
                df.loc[df['Name'] == name.lower(), 'amount'] += amount
                
                df['amount'] = df['amount'].clip(lower=0)
                
                self.saveInventory(df)
                
                return f"{name.lower()} increased by {amount}"
            else:
                raise ValueError(f"{name} not in inventory, nothing changed")
            
        except Exception as e:
            print(e)

    #adds item to PERSONAL shopping list
    def addToList(self,name):
        df = self.getList()
        try:
            if(not name.lower() in df["Name"].values):
                df = df._append({'Name':name.lower(),'amount':1}, ignore_index=True)

                self.saveList(df)

                return f"{name.lower()} added to shopping list with amount {1}"
            else:
                raise ValueError(f"{name.lower()} already exists on list, nothing added")
        
        except Exception as e:
            print(e)
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
    
    #generates shopping list based on inventory
    def generateInventoryList(self, _):
        
        inventoryDF     = self.getInventory()
        inventoryListDF = self.getInventoryList()

        zeroQtyItems = inventoryDF[inventoryDF['amount']==0]


        inventoryListDF = pd.concat([inventoryListDF,zeroQtyItems], ignore_index=True)

        self.saveInventoryList(inventoryListDF)
        return inventoryListDF
    
    #concats PERSONAL list and Inventory list then drops duplicates
    def goShopping(self, _):    
        
        dfCombined = pd.concat([self.getList(),self.generateInventoryList()], ignore_index=True)
        self.saveShoppingList(dfCombined.drop_duplicates(subset=['Name']))

    def wentShopping(self, data):
        #data = {"item": amount, ...}
        pass

    def ranOut(self, name):
        pass
        #sets amount to 0
