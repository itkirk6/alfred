import database
from settings import number_words

db = database.Database()


class Command:
    def __init__(self, keyword, description, returnValue, action, response):
        self.keyword = keyword
        self.description = description
        self.returnValue = returnValue
        self.action = action
        self.response = response
    

    def execute(self, *args):
        return self.action(*args)



commands = {
    "add": Command("Add item to inventory", ["item"], db.addItem, "OK! Added <item> to inventory"),
    "remove": Command("Remove item from inventory", ["item"], db.removeItem, "OK! Removed <item> from inventory."),
    "ate": Command("Consumed/used some item", ["item", "int: amount"], db.justAte, "Got it. you ate <amount> <item>s."),
    "set": Command("Set the quantity of an item", ["item", "int: amount"], db.setInventoryQuantity, "Understood. You now have <amount> <item>s."),
    "shop": Command("Going shopping or needs shopping list", [], db.goShopping, "Ok, Your shopping list has been dispatched."),
    "receipt": Command("Coming back from a shopping trip or has receipt", ["int: total"], db.wentShopping, "Ok! Your Items have been added to your kitchen. If only I could have helped carry them in!"),
    "out": Command("Ran out of some item", ["item"], db.ranOut, "Gotcha. You'll have to buy that one soon. I'll remind you.")
}

