import database

db = database.Database()


class Command:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def execute(self):
        self.action()



# conditions
addItem = ".*\badd\b.*"  # "... add ..."
removeItem = "(?:remove|take off|get rid of|(?:i|we) don't want)"
justAte = "(?:i\s+just\s+ate|just\s+ate|i\s+ate|just\s+had|i\s+had)"
addInventoryQuantity = "(?:i\s+bought\s+some\s+more|i\s+bought\s+.*?\s+more|i\s+bought|(?:we|i)\s+have\s+.*?\s+more|(?:we|i)\s+got\s+.*?)"



commands = [
    Command(addItem, db.addItem),
    Command(removeItem, db.removeItem),
    Command(justAte, db.justAte),
    Command(addInventoryQuantity, db.addInventoryQuantity)
    
]
