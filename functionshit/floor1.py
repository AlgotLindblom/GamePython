import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='')
            time.sleep(speed)
        if nl:
            print('')
    
    def floor1(self):
            self.coolText('''The ancient stone gates creek as you enter the tower...''', 0.02, True)
            self.coolText('The large, circular room inside seems somhow bigger on the inside than it did from the outside.', 0.02, True)
            input('>')
            self.coolText('Opposing you is a stairway leading up onto the next floor.', 0.02, True)
            if input('Do you wish to proceed? Yes/No ').lower() != 'Yes':
                self.coolText('Too bad...', 0.5, True)
            print('You ', end='')
            self.coolText('slowly', 0.1, False)
            self.coolText(' approach the stairway.', 0.02, True)
            self.coolText('You see dark room at the top of the stairway. To your right is a sign that is unclear. ', 0.02, True)
            c1 = input('You can look closer at the sign. What do you do? look/stay ')
            if c1.lower() != 'Look':
                self.coolText(' You do not have any other choices. Looking at plack.... ')
            # Här kallar på gåt funktion.
    
T = Tower()
T.floor1()
        
