#spara olika av omvärdlens egenskaper under klassen tower.
#samt basic movemtn går också här.
import time

class tower:
    currentFloor = 0
    floorDialogue = []
    items = []
    with open('items.txt') as f:
        for i in f.readlines():
            if i != '':
                items.append(i[:-1])

    def __init__(self) -> None:
        pass

    def coolText(self, text):
        for i in text:
            print(i, end='')
            time.sleep(0.1)
        print('')

    def nextFloor(self):
        return self.currentRoom + 1 
    
    def start(self):
        while True:
            welcome = input("Välkommen till tornet. Ditt mål är att ta dig till toppen. Är du ny till spelet? (Ja/Nej) ")
            if welcome == ("Ja").lower():
                print("För att gå kan du välja att gå Framåt ('F'), Bakåt ('B'), Höger ('H') eller Vänster ('V')")
                print("Det kommer stå i varje prompt vad du har för alternativ, så du behöver inte oroa dig vart du kan gå!")
                break
            elif welcome == ("Nej").lower():
                pass
            else:
                continue
            break
        print(f'''

    888
    888
    888                                           888
    888888 .d88b.  888 8888  888 88888    .d88b.  888 
    888   d88""88b 88888  88 88888   888 d8P  Y8b 888888
    888   888  888 888       888     888 88888888 888
    Y88b. Y88..88P 888       888     888 PY8b.    Y88b.
     "Y888 "Y88P   888       888     888   "Y8888  "Y888

               uuuuu
               |_#-|
               | _#|
               |_ -|
___.$$.________| - |____
  .#$$$. __    |-  |
  $$$$$$    ` -[__N]
  $$$$$$    -.
   `:/'    _.))
    ||  .'.-'
    '" /  (
      .    `.
      .      `--..
        ''')

#så här tänker jag vi kan hantera 
class towerFloor1:    
    def __init__(self):
        pass
    
    def nextFloor(self, inv):
        if 'key' in inv:
            tower.currentFloor = 2
        else:
            print('big error')

        
        
if __name__ == '__main__':
    #tl = tower(1)
    #tl.nextFloor()
    t = tower()
    t.start()
    tf2 = towerFloor1()
    tf2.nextFloor('key')
    print(tower.currentFloor)

