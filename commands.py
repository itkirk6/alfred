import database
from settings import number_words

db = database.Database()


class Command:
    def __init__(self, description, returnValue, action):
        self.description = description
        self.returnValue = returnValue
        self.action = action
    

    def execute(self, *args):
        return self.action(*args)



commands = {
    "add": Command("Add item to inventory", ["item", "int: amount"], db.addItem),
    "remove": Command("Remove item from inventory", ["item"], db.removeItem),
    "ate": Command("Consumed/used some item", ["item", "int: amount"], db.justAte),
    "set": Command("Set the quantity of an item", ["item", "int: amount"], db.setInventoryQuantity),
    "shop": Command("Going shopping or needs shopping list", ["bool: whether they asked for the list to be read"], db.goShopping),
    "receipt": Command("Coming back from a shopping trip or has receipt", ["int: total"], db.wentShopping),
    "out": Command("Ran out of some item", ["item"], db.ranOut)
}

