


class Command:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def execute(self):
        self.action()





def addToInventory_action():
    pass
addToInventory_condition = [
    ".*\badd\b.*",  # "... add ..." 
]


commands = [
    Command(addToInventory_condition, addToInventory_action)
]
