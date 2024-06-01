import database
from settings import number_words

db = database.Database()


class Command:
    def __init__(self, condition, action, parser):
        self.condition = condition
        self.action = action

    def execute(self, input_string, match):
        args = self.parser(input_string, match)
        return self.action(*args)



# conditions
addItem = ".*\badd\b.*"  # "... add ..."
removeItem = "(?:remove|take off|get rid of|(?:i|we) don't want)"
justAte = "(?:i\s+just\s+ate|just\s+ate|i\s+ate|just\s+had|i\s+had)"
addInventoryQuantity = "(?:i\s+bought\s+some\s+more|i\s+bought\s+.*?\s+more|i\s+bought|(?:we|i)\s+have\s+.*?\s+more|(?:we|i)\s+got\s+.*?)"
goShopping = "(?:shopping|walmart|to\s+the\s+store)"
wentShopping = "(?:went\s+shopping|bought\s+groceries|got\s+groceries|receipt)"
ranOut = "(?:out\s+of|ran\s+out|don'?t\s+have\s+any\s+more|no\s+more)"

# Parsing functions
def parse_addItem(input_string, match):
    # Example: "add apples 10"
    all = input_string.split("add")[1].split(" ")
    return (name, amount)

def parse_removeItem(input_string, match):
    # Example: "remove apples"
    parts = input_string.split()
    name = parts[1]
    return (name,)

def parse_justAte(input_string):
    # Example: "I just ate apples 3"
    parts = input_string.split()
    name = parts[3]
    amount = int(parts[4])
    return (name, amount)

def parse_addInventoryQuantity(input_string):
    # Example: "I bought more apples 5"
    parts = input_string.split()
    name = parts[-2]
    amount = int(parts[-1])
    return (name, amount)

def parseSimple(input_string):
    # For commands like goShopping, wentShopping, ranOut
    return (input_string,)
"""
commands = [
    Command(addItem, db.addItem),
    Command(removeItem, db.removeItem),
    Command(justAte, db.justAte),
    Command(addInventoryQuantity, db.addInventoryQuantity),
    Command(goShopping, db.goShopping),
    Command(wentShopping, db.wentShopping),
    Command(ranOut, db.ranOut)
]"""
