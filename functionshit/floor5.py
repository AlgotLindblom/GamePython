import time
import os
import random

#copied from main
class gamePlayer:
    inventory = [[[False, 0, "Dina händer", 1, "händer"], [True, 0, "Kort svärd", 3, "svärd"], [True, 1, "Simpel sköld", 4, "sköld"]], []] #index 0 is battle items

#copied from main 
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

class Tower:
    enemies = [["Skelett", 10, 10, 0, 0, 2, [0, 2, "Skelettet svingar sina armar mot dig"], [1, 2, "Skelettet förbereder sig för att ta din nästa attack"], "et"]["Fet goblin", 10, 10, 20, 0, 2, ["move 1"], ["move 2"], "en", ['Dö din ryggradslösa imbecill', 'Du stinker värre än vad jag gör', 'Du fick mig nästan!', 'Se upp så jag inte smäcker till dig med fläsket', 'Min farmor siktar bättre än dig', 'Kom ihåg vad Jesus en gång sa, pissa inte i motvind', 'Du träffa ju din chungus!', 'Låt mig vara, jag kommer sätta mig på dig', 'Du är bättre än vad man tror', 'Hade jag varit du hade jag sprungit', 'Död åt kungen', 'Ta mig i röva o kalla mig Bengt, det där gjorde ont']]]
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='', flush=True)
            time.sleep(speed)
        if nl:
            print('')

    def floor5(self):
        self.coolText('Du känner en skum lukt ju högre upp i trappan du kommer.', 0.02, True)
        self.coolText('Ett högt flåsande hörs och du börjar känna dig nervös.', 0.02, True)
        self.coolText('Ur skuggorna kommer en grovt överviktig, illaluktande Goblin.', 0.02, True)
        #Battle


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
                                                                     

                                

''', 0.0001, True)
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

''', 0.0001, True)


t = Tower()
t.floor5()