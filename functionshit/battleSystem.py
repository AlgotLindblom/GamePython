import os
import random
import time

class battleSystem:
    #enemies should probably be fetched from the tower floors info. Easy change
    enemies = [["skeleton", 10, 10, 0, 0, 2, [0, 2, "The skeleton swings at you"], [1, 3, "The skeleton braises itself for your next attack"]]] #name, current health, max health, current block, default block, amount of moves, move 1, move 2... (move type: 0: attack, 1: block)
    battleTools = [[False, 0, "Your fists", 1, "fist"], [True, 0, "Rusty sword", 3, "sword"], [True, 1, "Simple shield", 4, "shield"]] #if aquired, type, name, data value (types: 0: attack, 1: block)
    currentEnemy = None
    currentMove = [0, 0, ""] #temporarly store movetype, amount, name
    promptText = "> " #what to print when waiting for player choice
    waitText = "> " #what to print when waiting for player

    if __name__ == "__main__":
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
            availableTools.append(["Your fists", 0])
        
        print("\nYour move!")
        input(self.waitText)

        print("\nAvailable items:")
        for n in range(len(availableTools)):
            print(availableTools[n][0])
        print("\nWhat do you want to use?")
        loop = False
        while currentMove[2] == " ":
            if loop == True:
                print("\nThat is not a vaild item, choose another:")
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
                print(f"\nYou damage the {self.currentEnemy[0]} for {-(self.currentEnemy[3]-currentMove[1])} damage")
            else:
                self.currentEnemy[3] = self.currentEnemy[3] - currentMove[1]
                os.system("cls")
                self.printBattleStatus()
                print(f"\nThe {self.currentEnemy[0]} blocks your attack")
        elif currentMove[0] == 1:
            self.player[2] = self.player[2] + currentMove[1]
            os.system("cls")
            self.printBattleStatus()
            print(f"\nYou gain {currentMove[1]} block")
        input(self.waitText)

    def enemiesTurn(self):
        enemyMoves = []
        movePool = []
        currentEnemyMove = [0, 0, " "]
        print(f"\nThe {self.currentEnemy[0]}'s turn!")
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
                print(f"\n{currentEnemyMove[2]} and deals {-(self.player[2]-currentEnemyMove[1])} damage")
            else:
                self.currentEnemy[3] = self.currentEnemy[3] - self.currentMove[1]
                os.system("cls")
                self.printBattleStatus()
                print(f"\nYou block the {self.currentEnemy[0]}'s attack")
        elif currentEnemyMove[0] == 1:
            self.currentEnemy[3] = self.currentEnemy[3] + currentEnemyMove[1]
            os.system("cls")
            self.printBattleStatus()
            print(f"\n{currentEnemyMove[2]} and gains {currentEnemyMove[1]} block")
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
        print(f"{self.currentEnemy[0]} health:", end=" ")
        for p in range(len(healthBars[1])):
            print(healthBars[1][p], end=" ")
        print(f"\nYour health:", end=" ")
        for p in range(len(healthBars[0])):
            print(healthBars[0][p], end=" ")
        print("")

    #takes the id of the desired enemy in the enemy list, returns remaining health
    def startBattle(self, enemy):
        self.currentEnemy = self.enemies[enemy]
        self.currentEnemy.insert(len(self.currentEnemy), self.currentEnemy[1])
        os.system("cls")
        print(f"An enemy {self.currentEnemy[0]} attacks!")
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
        if self.player[0] > 0:  #if ur still alive
            return([True, self.player[0]])
        else:
            return([False, self.player[0]])


b = battleSystem()
b.startBattle(0)