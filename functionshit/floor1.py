import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='')
            time.sleep(speed)
        if nl:
            print('')
    
    def floor1(self):
            self.coolText('''The ancient stone gates creek as you enter the tower...''', 0.1, True)
            self.coolText('The large, circular room inside seems somhow bigger on the inside than it did from the outside. \n', 0.05, True)
            time.sleep(0.5)
            self.coolText('Opposing you is a stairway leading up onto the next floor.')
            if input('Do you wish to proceed? Yes/No ').lower() != 'Yes':
                self.coolText('Too bad...', True)
            print('You ', end='')
            self.coolText('slowly', False)
            print(' approach the stairway.\n')
    
T = Tower()
T.floor1()
        
