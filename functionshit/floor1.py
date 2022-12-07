import time

class Tower:
    def coolText(self, text, nl):
        for i in text:
            print(i, end='')
            time.sleep(0.1)
        if nl:
            print('')
    
    def floor1(self):
            self.coolText('''The ancient stone gates creek as you enter the tower...''', True)
            print('The large, circular room inside seems somhow bigger on the inside than it did from the outside. ')
            print('Opposing you is a stairway leading up onto the next floor.')
            if input('Do you wish to proceed? Yes/No ') != 'Yes':
                self.coolText('Too bad...', True)
            print('You ', end='')
            self.coolText('slowly', False)
            print(' approach the stairway.')
            
    
T = Tower()
T.floor1()
        
