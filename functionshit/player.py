class player:
    inventory = []
    def __init__(self):
        self.name = input('Vad heter du? \n')
    
    def vadheterjag(self):
        print(f'Du heter {self.name}')

    def newItem(self, item):
        self.inventory.append(item)

p = player()
p.vadheterjag()
l = p.vadheterjag().local
print(p.inventory)