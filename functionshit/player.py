class player:
    inventory = []
    def __init__(self):
        self.name = input('Vad heter du? \n')
    
    def vadheterjag(self):
        print(f'Du heter {self.name}')

    def newItem(self, item):
        self.inventory.append(item)
    
    def myInventory(self):
        for i in self.inventory:
            print(i)

p = player()
p.vadheterjag()
p.newItem(input('Va haru? '))
p.myInventory()