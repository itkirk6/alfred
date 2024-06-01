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



commands = [
    Command("Add item to inventory", ["item"], db.addItem),
    Command("Remove item from inventory", ["item"], db.removeItem),
    Command("Consumed/used some item", ["item", "int: amount"], db.justAte),
    #Command("", db.addInventoryQuantity),
    Command("Going shopping or needs shopping list", [], db.goShopping),
    Command("Coming back from a shopping trip or has receipt", [], db.wentShopping),
    Command("Ran out of some item", ["item"], db.ranOut)
]

