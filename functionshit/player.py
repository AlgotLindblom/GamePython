class player:
    def __init__(self):
        self.name = input('Vad heter du? \n')
    
    def vadheterjag(self):
        self.vadheterjag.local = 'local'
        print(f'Du heter {self.name}')

p = player()
p.vadheterjag()
l = p.vadheterjag().local
    