import os
debug = False


#paths
cwd = os.getcwd()
parent = os.path.dirname(cwd)

#to database
db = os.path.join(cwd,'db')
pathToInventory = os.path.join(db,"inventory.csv")
pathToPersonalList = os.path.join(db,"personalList.csv")
pathToInventoryList = os.path.join(db,"inventoryList.csv")
pathToShoppingList  = os.path.join(db, "shoppingList.csv")

