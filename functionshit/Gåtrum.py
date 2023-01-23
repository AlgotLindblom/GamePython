import time
import random


class Tower:
    def coolText(self, text, speed, nl): #text, float(smaller gives faster speed), True or False
        for i in text:
            print(i, end='', flush=True) #for some reason without"flush=True" this does not work as intended for me /karl
            time.sleep(speed)
        if nl:
            print('')

    def tressureRoom(self):
        self.coolText(f'''You crouch down almost having to crawl down the path
        You emerge from the path into a room full of candles where you see a glass stand with the number 5 on it.\n
        In the base of the stand you notice a cubic hole. Before you you see 3 boxes.
                                        _____                                   
                                4_   /
        On the first box it says :  \_/   625
        \n                                   
        On the second box it says : x < 0  x^2=25
        \n
        On the third box it says : |x-7| = 25
        ''')
        while True: 
            match int(input('One of the 3 boxes will fit in the hole\nWhich one do you choose?')):
                case 1:
                    self.coolText(f''''När du placerar in lådan så hör du ett muller och hur glass monter med ett POP försvinner in i tomma luften.
                                I dess plats så står det ett elegant svärd i blankt stål
                        ''')
                case 2:
                    self.coolText(f'''' Du hör ett rummel och ser hur en yxa susar ut ur väggen rakt framför dig!''', 0.02, True)
                    match input(f''' 
                            Vilket håll vill du undvika åt? Höger eller vänster?''').lower():
                            case 'höger':
                                self.coolText('Du hoppar åt höger', 0.02, True)

                            case 'vänster':
                                self.coolText('Du hoppar åt vänster', 0.02, True)
                               
                            case other:
                                print('död')
                    if bool(random.getrandbits(1)):
                        #ta livet av dom 
                        print('död')
                case 3: 
                    self.coolText(f'''' Du hör en främmande röst messa genom rummet. Och känner värmen mot din hud.  ''')
            break


    def riddle():
        firstplack = 0
        while True:
            if firstplack == 0:
                print('När du kommer upp för trappen ser du en kort korridor som sen delar sig in till två gångar.')
                print('Precis där vägen delar sig ser du en tavla som säger')
                print(f''''
                _   _               _   _   _                                            _                       _   _                   _   
                | | | |             | | | | | |                                          | |                     | | | |                 | |  
                | |_| | ___  ___  __| | | |_| |__   ___  ___  ___  __      _____  _ __ __| |___    __ _ _ __   __| | | |__   ___  ___  __| |  
                |  _  |/ _ \/ _ \/ _` | | __| '_ \ / _ \/ __|/ _ \ \ \ /\ / / _ \| '__/ _` / __|  / _` | '_ \ / _` | | '_ \ / _ \/ _ \/ _` |  
                | | | |  __/  __/ (_| | | |_| | | |  __/\__ \  __/  \ V  V / (_) | | | (_| \__ \ | (_| | | | | (_| | | | | |  __/  __/ (_| |  
                \_| |_/\___|\___|\__,_|  \__|_| |_|\___||___/\___|   \_/\_/ \___/|_|  \__,_|___/  \__,_|_| |_|\__,_| |_| |_|\___|\___|\__,_|  
                                                                                                                                            
                                                                                                                                            
                _   _     _                   _   _         _____     _          _   _                            _                          
                | | | |   (_)                 | | | |       |_   _|   | |        | | | |                          | |                         
                | |_| |__  _ ___   _ __   __ _| |_| |__       | | __ _| | _____  | |_| |__   ___   _ __ ___  _   _| |_ ___                    
                | __| '_ \| / __| | '_ \ / _` | __| '_ \      | |/ _` | |/ / _ \ | __| '_ \ / _ \ | '__/ _ \| | | | __/ _ \                   
                | |_| | | | \__ \ | |_) | (_| | |_| | | |_    | | (_| |   <  __/ | |_| | | |  __/ | | | (_) | |_| | ||  __/                   
                \__|_| |_|_|___/  | .__/ \__,_|\__|_| |_(_)   \_/\__,_|_|\_\___|  \__|_| |_|\___| |_|  \___/ \__,_|\__\___|                   
                                | |                                                                                                         
                                |_|                                                                                                         
                        __                            _                     _                   __          _   _ _    ______ _           _   
                    / _|                             | |                   | |                 / _|        | | (_) |   | ___ \ |         | |  
                ___  | |_    _   _  ___  _   _ _ __  | |__   ___  __ _ _ __| |_    ___  _ __  | |_ ___  ___| |  _| |_  | |_/ / | __ _ ___| |_ 
                / _ \|  _|  | | | |/ _ \| | | | '__| | '_ \ / _ \/ _` | '__| __|  / _ \| '__| |  _/ _ \/ _ \ | | | __| | ___ \ |/ _` / __| __|
                | (_) | |   | |_| | (_) | |_| | |    | | | |  __/ (_| | |  | |_  | (_) | |    | ||  __/  __/ | | | |_  | |_/ / | (_| \__ \ |_ 
                \___/|_|    \__, |\___/ \__,_|_|    |_| |_|\___|\__,_|_|   \__|  \___/|_|    |_| \___|\___|_| |_|\__| \____/|_|\__,_|___/\__|
                            __/ |                                                                                                           
                            |___/                                                                                                             
                ''')
            elif firstplack == 1:
                print('När du öppnar ögonen står du igen framför samma tavla')
                print(f''''
                _   _               _   _   _                                            _                       _   _                   _   
                | | | |             | | | | | |                                          | |                     | | | |                 | |  
                | |_| | ___  ___  __| | | |_| |__   ___  ___  ___  __      _____  _ __ __| |___    __ _ _ __   __| | | |__   ___  ___  __| |  
                |  _  |/ _ \/ _ \/ _` | | __| '_ \ / _ \/ __|/ _ \ \ \ /\ / / _ \| '__/ _` / __|  / _` | '_ \ / _` | | '_ \ / _ \/ _ \/ _` |  
                | | | |  __/  __/ (_| | | |_| | | |  __/\__ \  __/  \ V  V / (_) | | | (_| \__ \ | (_| | | | | (_| | | | | |  __/  __/ (_| |  
                \_| |_/\___|\___|\__,_|  \__|_| |_|\___||___/\___|   \_/\_/ \___/|_|  \__,_|___/  \__,_|_| |_|\__,_| |_| |_|\___|\___|\__,_|  
                                                                                                                                            
                                                                                                                                            
                _   _     _                   _   _         _____     _          _   _                            _                          
                | | | |   (_)                 | | | |       |_   _|   | |        | | | |                          | |                         
                | |_| |__  _ ___   _ __   __ _| |_| |__       | | __ _| | _____  | |_| |__   ___   _ __ ___  _   _| |_ ___                    
                | __| '_ \| / __| | '_ \ / _` | __| '_ \      | |/ _` | |/ / _ \ | __| '_ \ / _ \ | '__/ _ \| | | | __/ _ \                   
                | |_| | | | \__ \ | |_) | (_| | |_| | | |_    | | (_| |   <  __/ | |_| | | |  __/ | | | (_) | |_| | ||  __/                   
                \__|_| |_|_|___/  | .__/ \__,_|\__|_| |_(_)   \_/\__,_|_|\_\___|  \__|_| |_|\___| |_|  \___/ \__,_|\__\___|                   
                                | |                                                                                                         
                                |_|                                                                                                         
                        __                            _                     _                   __          _   _ _    ______ _           _   
                    / _|                             | |                   | |                 / _|        | | (_) |   | ___ \ |         | |  
                ___  | |_    _   _  ___  _   _ _ __  | |__   ___  __ _ _ __| |_    ___  _ __  | |_ ___  ___| |  _| |_  | |_/ / | __ _ ___| |_ 
                / _ \|  _|  | | | |/ _ \| | | | '__| | '_ \ / _ \/ _` | '__| __|  / _ \| '__| |  _/ _ \/ _ \ | | | __| | ___ \ |/ _` / __| __|
                | (_) | |   | |_| | (_) | |_| | |    | | | |  __/ (_| | |  | |_  | (_) | |    | ||  __/  __/ | | | |_  | |_/ / | (_| \__ \ |_ 
                \___/|_|    \__, |\___/ \__,_|_|    |_| |_|\___|\__,_|_|   \__|  \___/|_|    |_| \___|\___|_| |_|\__| \____/|_|\__,_|___/\__|
                            __/ |                                                                                                           
                            |___/                                                                                                             
                ''')
            directionChoice_1 = str(input('Which pathway do you choose? To the Right or to the Left\n').lower)
            if directionChoice_1 == 'R' or 'Right':
                firstplack + 1
                print('You walk down the pathway, all of a sudden ')
            elif directionChoice_1 == 'L' or 'Left':
                print('Choosing the pathway to the left you start walking.\nAfter a while you find a small crouching path to the left')
