import os
import random
import time

#Här sparas spelar karaktärens egenskaper.
class gamePlayer:
    inventory = [[[False, 0, "Dina händer", 1, "händer"], [True, 0, "Kort svärd", 3, "svärd"], [True, 1, "Simpel sköld", 4, "sköld"]], []] #index 0 is battle items
    health = []
    player = [10, 10, 0, 0]
    def __init__(self):
        self.name = input('Vad heter du? \n')
    
    def vadheterjag(self):
        print(f'Du heter {self.name}')

    def newItem(self, item):
        self.inventory.append(item)
    
    def playerDeath(self):
        print()
        #kör catbomb


#spara olika av omvärdlens egenskaper under klassen tower.
#samt basic movemtn går också här.
class tower:
    currentFloor = [[]]
    enemies = [["Skelett", 10, 10, 0, 0, 2, [0, 2, "Skelettet svingar sina armar mot dig"], [1, 2, "Skelettet förbereder sig för att ta din nästa attack"], "et"]]
    floorDialogue = []
    items = []
    #Kommer behöva titta över detta sen
    if False:
        with open(os.getcwd()+r'\functionshit\items.txt') as f:
            for i in f.readlines():
                if i != '':
                    items.append(i[:-1])

    def __init__(self):
        pass
    
    def coolText(self, text, speed, nl): #text, float(smaller gives faster speed), True or False
        for i in text:
            print(i, end='', flush=True) #for some reason without"flush=True" this does not work as intended for me /karl
            time.sleep(speed)
        if nl:
            print('')

    def nextRoom(self):
        self.currentRoom += 1 #currentRoom is not defined?
    
    def start(self):
        while True:
            self.coolText("Spela detta spel i kommandotolken i fullscreenläge för att grafiken ska funka.", 0.001, True)
            welcome = input("Välkommen till tornet. Ditt mål är att ta dig till toppen. Är du ny till spelet? (Ja/Nej) ").lower()
            if welcome == ("nej"):
                continue
            if welcome != ("ja"):
                continue
            print("För att gå kan du välja att gå Framåt ('F'), Bakåt ('B'), Höger ('H') eller Vänster ('V')")
            print("Det kommer stå i varje prompt vad du har för alternativ, så du behöver inte oroa dig vart du kan gå!")
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

    #Jag tycker att rummen ska följa denna template för dialog. då får vi lite consitancy.
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


    def floor3(self):
        temp = False
        self.coolText('Du känner en kall bris över din rygg när du går upp för trappan', 0.02, True)
        self.coolText('Månens ljus slinkras igenom i den trasig torn väggen och lyser upp rummet framför dig', 0.02, True)
        self.coolText('I rummet finns det två dörrar', 0.02, True)
        self.coolText('Den vänstra dörren ser ut att vara en trädörr med en skylt som säger *Varning* på', 0.02, True)
        self.coolText('Den högra dörren ser ut att vara en vanlig trädörr', 0.02, True)
        högerFörsök = 0
        while temp == False:
            self.coolText("Vill du gå igenom den högra eller den vänstra dörren?", 0.02, True)
            do = input('> ').lower()
            if ("höger" in do) or ("högra" in do):
                self.coolText('Du försöker öppna den högra dörren men den vägrar röra på sig', 0.02, True)
                self.coolText("Dörren är låst", 0.02, True)
                self.coolText("Du ger upp och försöker öppna den vänstra dörren istället", 0.02, True)
                högerFörsök += 1
                temp = True
            elif ("vänster" in do) or ("vänstra" in do):
                self.coolText("Du går fram till och försöker öppna den vänstra dörren", 0.02, True)
                temp = True
            else:
                self.coolText("Vänta vad sa du?", 0.02, True)
        self.coolText('Dörren knakar högt medans du öppnar den', 0.02, True)
        self.coolText('Rummet bakom dörren är tomt förutom att i mitten av rummet står ett mänskligt skelett', 0.02, True)
        self.coolText('Runt halsen på skelettet hänger en nyckel på en kedja', 0.02, True)
        if högerFörsök > 0:
            self.coolText('Kan detta vara nyckeln till den högra dörren?', 0.02, True)
        self.coolText('Medans du stirrar på skelettet börjar det glöda rött i dess ögon och skelettet börjar röra på sig', 0.02, True)
        self.coolText('Skelettet attackerar dig!', 0.02, True)
        input("> ")
        bs.startTutorialBattle()

        self.coolText('Du besegrade skelettet som nu ligger i bitar på golvet', 0.02, True)
        self.coolText('Du tar nyckeln som hängde runt dess hals', 0.02, True)
        if högerFörsök > 0:
            self.coolText('Kan detta vara nyckeln till den första dörren?', 0.02, True)
            self.coolText('Du går tillbaka och låser upp den första dörren', 0.02, True)
        else:
            self.coolText('Med att skelettet återigen är död så finns det inget mer att göra i rummet', 0.02, True)
            self.coolText('Du går då tillbaka till det första rummet där det fanns en till dörr', 0.02, True)
            self.coolText('Du försöker öppna den andra dörren men upptäcker att den är låst', 0.02, True)
            self.coolText('Du snabbt låser upp dörren med nyckeln du presis hittade', 0.02, True)
        self.coolText('Dörren öppnas till en trappa till nästa våning', 0.02, True)
        # Kalla på våning 4

    def floor4(self):
        self.coolText('Du går upp för ännu en trappa', 0.02, True)
        self.coolText('Du kollar ut genom en springa i väggen och märker att du är väldigt högt upp', 0.02, True)
        self.coolText('Du möts av en mörk korridor. Det finns en dörr rakt fram och en till höger', 0.02, True)
        if input('Var vill du gå? (Fram/Höger) ').lower() != 'fram':
            self.coolText('Du går fram till dörren och drar i handtaget', 0.02, True)
            self.coolText('Dörren är låst och du väljer att gå till den andra dörren', 0.02, True)
            pass
        self.coolText('Du öppnar dörren', 0.02, True)
        bs.startBattle(["gargoyle", 2, 2, 8, 0, 2, [0, 3, "Gargoylen biter dig"], [1, 2, "Gargoylen stirrar starkt på dig"], "en"])

        self.coolText('Efter att du besegrat besten går du tillbaka ut i korridoren. Dörren som nu är till vänster om dig verkar stå på glänt.', 0.02, True)
        self.coolText('Du öppnar den och känner en bris av varm luft komma mot dig.', 0.02, True)
        self.coolText('Du börjar gå upp för trappan.', 0.02, True)
        # Kalla på våning 5 (bossfight)

    def floor5(self):
        self.coolText('Du känner en skum lukt ju högre upp i trappan du kommer.', 0.02, True)
        self.coolText('Ett högt flåsande hörs och du börjar känna dig nervös.', 0.02, True)
        self.coolText('Ur skuggorna kommer en grovt överviktig, illaluktande Goblin som överfaller dig.', 0.02, True)
        
        input("> ")
        bs.startBossBattle()


        self.coolText('''

  ______                         __        __      __            __       
 /      \                       |  \      |  \    |  \          |  \      
|  $$$$$$\  ______    ______   _| $$_    _| $$_    \$$  _______ | $$      
| $$ __\$$ /      \  |      \ |   $$ \  |   $$ \  |  \ /       \| $$      
| $$|    \|  $$$$$$\  \$$$$$$\ \$$$$$$   \$$$$$$  | $$|  $$$$$$$| $$      
| $$ \$$$$| $$   \$$ /      $$  | $$ __   | $$ __ | $$ \$$    \  \$$      
| $$__| $$| $$      |  $$$$$$$  | $$|  \  | $$|  \| $$ _\$$$$$$\ __       
 \$$    $$| $$       \$$    $$   \$$  $$   \$$  $$| $$|       $$|  \      
  \$$$$$$  \$$        \$$$$$$$    \$$$$     \$$$$  \$$ \$$$$$$$  \$$      
                                                                          
                                                                          
                                                                          
 _______                                                                  
|       \                                                                 
| $$$$$$$\ __    __        __     __   ______   _______   _______         
| $$  | $$|  \  |  \      |  \   /  \ |      \ |       \ |       \        
| $$  | $$| $$  | $$       \$$\ /  $$  \$$$$$$\| $$$$$$$\| $$$$$$$\       
| $$  | $$| $$  | $$        \$$\  $$  /      $$| $$  | $$| $$  | $$       
| $$__/ $$| $$__/ $$         \$$ $$  |  $$$$$$$| $$  | $$| $$  | $$       
| $$    $$ \$$    $$          \$$$    \$$    $$| $$  | $$| $$  | $$       
 \$$$$$$$   \$$$$$$            \$      \$$$$$$$ \$$   \$$ \$$   \$$       
                                                                     

                                

''', 0.00001, True)
        self.coolText('''

  ______   __                                        __                                    
 /      \ |  \                                      |  \                                   
|  $$$$$$\| $$   __   ______    ______    ______   _| $$_           ______   __     __  __ 
| $$___\$$| $$  /  \ |      \  /      \  |      \ |   $$ \         |      \ |  \   /  \|  \+
 \$$    \ | $$_/  $$  \$$$$$$\|  $$$$$$\  \$$$$$$\ \$$$$$$          \$$$$$$\ \$$\ /  $$ \$$
 _\$$$$$$\| $$   $$  /      $$| $$  | $$ /      $$  | $$ __        /      $$  \$$\  $$  __ 
|  \__| $$| $$$$$$\ |  $$$$$$$| $$__/ $$|  $$$$$$$  | $$|  \      |  $$$$$$$   \$$ $$  |  \+
 \$$    $$| $$  \$$\ \$$    $$| $$    $$ \$$    $$   \$$  $$       \$$    $$    \$$$    \$$
  \$$$$$$  \$$   \$$  \$$$$$$$| $$$$$$$   \$$$$$$$    \$$$$         \$$$$$$$     \$        
                              | $$                                                         
                              | $$                                                         
                               \$$                                                         
  ______                                                                                   
 /      \                                                                                  
|  $$$$$$\  _______   _______                                                              
| $$  | $$ /       \ /       \                                                             
| $$  | $$|  $$$$$$$|  $$$$$$$                                                             
| $$  | $$ \$$    \  \$$    \                                                              
| $$__/ $$ _\$$$$$$\ _\$$$$$$\                                                             
 \$$    $$|       $$|       $$                                                             
  \$$$$$$  \$$$$$$$  \$$$$$$$          

''', 0.00001, True)



class battleSystem:
    #enemies should probably be fetched from the tower floors info. Easy change
    #enemies = [["skeleton", 10, 10, 0, 0, 2, [0, 2, "The skeleton swings at you"], [1, 3, "The skeleton braises itself for your next attack"], "et"]] #name, current health, max health, current block, default block, amount of moves, move 1, move 2... (move type: 0: attack, 1: block)
    battleTools = gamePlayer.inventory[0] #if aquired, type, name, data value (types: 0: attack, 1: block)
    currentEnemy = None
    currentMove = [0, 0, ""] #temporarly store movetype, amount, name
    promptText = "> " #what to print when waiting for player choice
    waitText = "> " #what to print when waiting for player
    player = [10, 10, 0, 0] #current health, max health, current block, default block
    
    def __init__(self) -> None:
        pass

    def playersTurn(self):
        currentMove = [0, 0, " "]
        availableTools = []
        battleTools = self.battleTools
        for w in range(len(battleTools)):
            if battleTools[w][0] == True:
                availableTools.append([battleTools[w][2], w])
        if len(availableTools) == 0: #if no weapons adds fists as option
            availableTools.append(["Dina händer", 0])
        
        print("\nDin tur!") 
        input(self.waitText)

        print("\nTillgängliga verktyg:") 
        for n in range(len(availableTools)):
            print(availableTools[n][0])
        print("\nVilken vill du använda?")
        loop = False
        while currentMove[2] == " ":
            if loop == True:
                print("\nDet är inte en tillgänglig verktyg, välj en annan:")
            loop = True
            do = input(self.promptText)
            for t in range(len(availableTools)):
                if battleTools[availableTools[t][1]][4] in do.lower():
                    currentMove[0] = battleTools[availableTools[t][1]][1] #saves current move [0] to move type
                    currentMove[1] = battleTools[availableTools[t][1]][3] #saves current move [1] to move data (how much damage/block)
                    currentMove[2] = battleTools[availableTools[t][1]][2] #saves name of move
        if currentMove[0] == 0:
            if self.currentEnemy[3]-currentMove[1] < 0:
                self.currentEnemy[1] = self.currentEnemy[1] + (self.currentEnemy[3] - currentMove[1])
                self.currentEnemy[3] = 0
                os.system("cls")
                self.printBattleStatus()
                print(f"\nDu skadar {self.currentEnemy[0]}{self.currentEnemy[8]} för {-(self.currentEnemy[3]-currentMove[1])} skada")
            else:
                self.currentEnemy[3] = self.currentEnemy[3] - currentMove[1]
                os.system("cls")
                self.printBattleStatus()
                print(f"\n{self.currentEnemy[0]}{self.currentEnemy[8]}  blockerar din attack")
        elif currentMove[0] == 1:
            self.player[2] = self.player[2] + currentMove[1]
            os.system("cls")
            self.printBattleStatus()
            print(f"\nDu får {currentMove[1]} block")
        input(self.waitText)

    def enemiesTurn(self):
        enemyMoves = []
        movePool = []
        currentEnemyMove = [0, 0, " "]
        print(f"\n{self.currentEnemy[0]}{self.currentEnemy[8]}s tur!")
        input(self.waitText)
        for m in range(self.currentEnemy[5]):
            enemyMoves.append(self.currentEnemy[6+m]) #load enemies moves into temp variables
            if (enemyMoves[m][0] == 0) and (enemyMoves[m][1] >= self.player[0]): #if move is damage, and lethal then add to movepool (if can kill in one hit it will use damage move)
                movePool.append(enemyMoves[m])
        if len(movePool) == 0: #if no moves in pool, will ad every move
            for m in range(len(enemyMoves)):
                movePool.append(enemyMoves[m])
        currentEnemyMove = movePool[random.randint(0, len(movePool)-1)]
        if currentEnemyMove[0] == 0:
            if self.player[2]-currentEnemyMove[1] < 0:
                self.player[0] = self.player[0] + (self.player[2] - currentEnemyMove[1])
                self.player[2] = 0
                os.system("cls")
                self.printBattleStatus()
                print(f"\n{currentEnemyMove[2]} and gör {-(self.player[2]-currentEnemyMove[1])} skada")
            else:
                self.player[2] = self.player[2] - currentEnemyMove[1]
                os.system("cls")
                self.printBattleStatus()
                print(f"\ndu blockerar {self.currentEnemy[0]}{self.currentEnemy[8]}s attack")
        elif currentEnemyMove[0] == 1:
            self.currentEnemy[3] = self.currentEnemy[3] + currentEnemyMove[1]
            os.system("cls")
            self.printBattleStatus()
            print(f"\n{currentEnemyMove[2]} och får {currentEnemyMove[1]} block")
        input(self.waitText)
        

    def printBattleStatus(self):
        healthBars = [[], []] #0'th is player, 1'th is enemy's
        for h in range(self.player[1]-self.player[0]):
            healthBars[0].insert(0, "□")
        for h in range(self.player[0]):
            healthBars[0].insert(0, "■")
        for h in range(self.currentEnemy[2]-self.currentEnemy[1]):
            healthBars[1].insert(0, "□")
        for h in range(self.currentEnemy[1]):
            healthBars[1].insert(0, "■")
        print(f"{self.currentEnemy[0]} hälsa:", end=" ")
        for p in range(len(healthBars[1])):
            print(healthBars[1][p], end=" ")
        print(f"{self.currentEnemy[0]} block: {self.currentEnemy[3]}", end=" ")
        print(f"\nDin hälsa:", end=" ")
        for p in range(len(healthBars[0])):
            print(healthBars[0][p], end=" ")
        print(f"Din block: {self.player[2]}", end=" ")
        print("")

    #takes the id of the desired enemy in the enemy list, returns [True/False if player won battle, remaining health]
    def startBattle(self, enemy):
        try:
            self.player = gamePlayer.player
        except:
            self.player = [10, 10, 0, 0]
        self.currentEnemy = enemy.copy()
        self.currentEnemy.insert(len(self.currentEnemy), self.currentEnemy[1])
        os.system("cls")
        print(f"Ett fientligt {self.currentEnemy[0]} attackerar!")
        input(self.waitText)
        while (self.currentEnemy[1] > 0) and (self.player[0] > 0 ):
            os.system("cls")
            self.printBattleStatus()
            time.sleep(0.5)
            self.playersTurn()
            os.system("cls")
            if self.currentEnemy[1] > 0:
                self.printBattleStatus()
                time.sleep(0.5)
                self.enemiesTurn()
        gamePlayer.player = self.player
        if self.player[0] > 0:  #if ur still alive
            return([True, self.player[0]])
        else:
            return([False, self.player[0]])
    
    def startTutorialBattle(self): #has preset tutorial enemy
        self.currentEnemy = ["Skelett", 10, 10, 0, 0, 2, [0, 2, "Skelettet svingar sina armar mot dig"], [1, 2, "Skelettet förbereder sig för att ta din nästa attack"], "et"]
        os.system("cls")
        print(f"Ett fientligt {self.currentEnemy[0]} attackerar!")
        input(self.waitText)
        print("I strid turas du och din fiende om att använda verktyg")
        input(self.waitText)
        print("verktyg du använder antingen skadar din fiende eller ger dig själv block vilket blockerar skada från fiendens nästa attack")
        input(self.waitText)
        print("Om fiendens hälsa når 0 vinner du striden och kan fortsätta äventyra medans om din hälsa når 0 förlorar du")
        input(self.waitText)
        os.system("cls")
        self.printBattleStatus()
        time.sleep(0.5)
        self.playersTurn()
        if self.currentEnemy[1] > 0:
            print("Nu är det fiendens tur")
            input(self.waitText)
            print("Fienden kan också antingen attackera dig eller generera block")
            input(self.waitText)
            print("Fienden bästemer vad den gör nästan slumpmässigt")
            input(self.waitText)
            os.system("cls")
            self.printBattleStatus()
            time.sleep(0.5)
            self.enemiesTurn()
        while (self.currentEnemy[1] > 0) and (self.player[0] > 0 ):
            os.system("cls")
            self.printBattleStatus()
            time.sleep(0.5)
            self.playersTurn()
            os.system("cls")
            if self.currentEnemy[1] > 0:
                self.printBattleStatus()
                time.sleep(0.5)
                self.enemiesTurn()
        gamePlayer.player = self.player
        if self.player[0] > 0:  #if ur still alive
            return([True, self.player[0]])
        else:
            return([False, self.player[0]])

    def startBossBattle(self):
        try:
            self.player = gamePlayer.player
        except:
            self.player = [10, 10, 0, 0]
        self.currentEnemy = ["Fet goblin", 25, 25, 0, 0, 2, [0, 3, "goblinen tacklar dig"], [0, 2, "goblinen spottar syra på dig"], "en", ['Dö din ryggradslösa imbecill!', 'Du stinker värre än vad jag gör!', 'Du fick mig nästan!', 'Se upp så jag inte smäcker till dig med fläsket!', 'Min farmor siktar bättre än dig!', 'Kom ihåg vad Jesus en gång sa, pissa inte i motvind!', 'Du träffa ju din chungus!', 'Låt mig vara, jag kommer sätta mig på dig!', 'Du är bättre än vad man tror!', 'Hade jag varit du hade jag sprungit!', 'Död åt kungen!', 'Ta mig i röva o kalla mig Bengt, det där gjorde ont!']]
        os.system("cls")
        print(f"En fientlig {self.currentEnemy[0]} attackerar!")
        input(self.waitText)
        while (self.currentEnemy[1] > 0) and (self.player[0] > 0 ):
            os.system("cls")
            self.printBattleStatus()
            time.sleep(0.5)
            self.playersTurn()
            os.system("cls")
            if self.currentEnemy[1] > 0:
                self.printBattleStatus()
                time.sleep(0.5)
                self.enemiesTurn()
                if random.randrange(0, 2) == 1:
                    print("\nGoblinen skriker fula ord åt dig")
                    print(self.currentEnemy[9][random.randrange(0, len(self.currentEnemy[9]))])
                    input("> ")
        gamePlayer.player = self.player
        if self.player[0] > 0:  #if ur still alive
            return([True, self.player[0]])
        else:
            return([False, self.player[0]])


if __name__ == '__main__':
    gp = gamePlayer()
    tw = tower()
    bs = battleSystem()
    def floor():
        bs.startBattle(tw.enemies[0])
    floor()
    bs.startBattle(tw.enemies[0])

    #bs.startBattle(["skeleton", 10, 10, 0, 0, 2, [0, 2, "The skeleton swings at you"], [1, 3, "The skeleton braises itself for your next attack"]]) #hihi
    
    #print(p.inventory)
    #p.newItem('sword')
    #print(p.inventory)
