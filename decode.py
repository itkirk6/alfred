
class Decode:
    def __init__(self,command):
        self.value = self.decodeCommand(command)
    
    #command should look like this -> add 3 oranges / remove 1 milk / ate 2 steak / 
    def decodeCommand(self,command): # returns data to captured, [str commandName,str itemName,int ammount] or False
        command = command.split(" ")
        if len(command) == 3:
            return[command[0],command[2],command[1]]
        else:
            return False
        
        