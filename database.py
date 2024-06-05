import settings
import datetime
import pandas as pd
import random
import outputChoices
import printer

class Database:
    def __init__(self):
        pass

    def getInventory(self):
        return pd.read_csv(settings.pathToInventory, dtype={"amount": int})

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
    def addItem(self, name, amount): #returns string
            
        df = self.getInventory()
        print(df)

        try:
            if(not df.isin([name.lower()]).any().any()):
                df = df._append({'name':name.lower(),'amount': amount}, ignore_index=True)
                
                self.saveInventory(df)
                #df.to_csv(settings.pathToInventory, index=False)

                return f"Got it! I added {name}s to your inventory."
            else:
                return f"{name}s already exist in your inventory, nothing added"
        
        except Exception as e:
            print(e)
            return "There was an error adding your item to the inventory."
    

    # removes item from inventory
    def removeItem(self, name): #returns string
        
        df = self.getInventory()

        try:

            if(name.lower() in df["name"].values):
                
                df = df[df['name'] != name.lower()]
                
                self.saveInventory(df)
                #df.to_csv(settings.pathToInventory,index=False)
                return f"Success! Removed {name} from the inventory."
            else:
                return f"{name} does not exist in inventory, nothing removed"
        except Exception as e:
            print(e)
            return "There was an error removing your item from the inventory."
    
    # reduces inventory quantity by amount
    def justAte(self, name, amount):
        amount = int(amount)

        df = self.getInventory()
        try:
            if name.lower() in df["name"].values:
                #print(type(df.loc[df['name'] == name.lower(), 'amount'].values[0]))
                df.loc[df['name'] == name.lower(), 'amount'] -= amount
                
                df['amount'] = df['amount'].clip(lower=0)
                
                self.saveInventory(df)
                
                if random.random() > 0.5:
                    return f"Noted. you now have {df.loc[df['name'] == name.lower(), 'amount'].iloc[0]} {name}."
                else:
                    return random.choice(outputChoices.ateItem)
            else:
                return(f"{name} is not in your inventory, nothing changed")
            
        except Exception as e:
            print(e)
            return "There was an error interfacing with your inventory."
    
    # increases inventory quantity by amount
    def setInventoryQuantity(self, name, amount):
        amount = int(amount)
        df = self.getInventory()

        try:

            if name.lower() in df["name"].values:
                
                df.loc[df['name'] == name.lower(), 'amount'] = amount
                #df['amount'] = df['amount'].clip(lower=0)
                self.saveInventory(df)
                
                return f"Gotcha. You now have {amount} {name}s."
            else:
                return f"{name} is not in your inventory, nothing changed"
            
        except Exception as e:
            print(e)
            return "There was an error interfacing with your inventory."

    """
    #adds item to PERSONAL shopping list
    def addToList(self,name):
        df = self.getList()
        try:
            if(not name.lower() in df["name"].values):
                df = df._append({'name':name.lower(),'amount':1}, ignore_index=True)

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

            if(name.lower() in df["name"].values):
                
                df = df[df['name'] != name.lower()]
                
                self.saveList(df)
                return f"{name.lower()} removed from list"
            else:
                raise ValueError(f"{name.lower()} does not exist in list, nothing removed")
        except Exception as e:
            print(e)
    """

    def goShopping(self, wantsRead):
        inventoryDF     = self.getInventory()
        inventoryListDF = self.getInventoryList()

        zeroQtyItems = inventoryDF[inventoryDF['amount']==0]


        #inventoryListDF = pd.concat([inventoryListDF,zeroQtyItems], ignore_index=True)

        #self.saveInventoryList(inventoryListDF)
        if wantsRead == "False":
            # somehow print this: inventoryListDF
            printer.printShoppingList(zeroQtyItems)
            return "OK! I have printed your shopping list."
        
        else:
            inventoryItemsSpeech = ' '.join(zeroQtyItems['name'])
            inventorySpeech = f"Here is your shopping list: {inventoryItemsSpeech}"

            if random.random() < 0.5:
                inventorySpeech += f". You should maybe cut down on the {inventoryListDF['name'].sample().iloc[0]}s since they are gross."

            return inventorySpeech



    def wentShopping(self, total):
        pass



    def ranOut(self, name):
        return self.setInventoryQuantity(name, "0")
