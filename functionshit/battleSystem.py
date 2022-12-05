import os
import random
import time
enemies = [["skeleton", 10, 10, 0, 0, 2, [0, 2, "The skeleton swings at you"], [1, 3, "The skeleton braises itself for your next attack"]]] #name, current health, max health, current block, default block, amount of moves, move 1, move 2... (move type: 0: attack, 1: block)
battleTools = [[False, 0, "Your fists", 1, "fist"], [True, 0, "Rusty sword", 3, "sword"], [True, 1, "Simple shield", 4, "shield"]] #if aquired, type, name, data value (types: 0: attack, 1: block)
currentEnemy = None
currentMove = [0, 0, ""] #temporarly store movetype, amount, name
promptText = "> " #what to print when waiting for player choice
waitText = "> " #what to print when waiting for player

if __name__ == "__main__":
    player = [10, 10, 0, 0] #current health, max health, current block, default block

def playersTurn():
    currentMove = [0, 0, " "]
    availableTools = []
    for w in range(len(battleTools)):
        if battleTools[w][0] == True:
            availableTools.append([battleTools[w][2], w])
    if len(availableTools) == 0: #if no weapons adds fists as option
        availableTools.append(["Your fists", 0])
    
    print("\nYour move!")
    input(waitText)

    print("\nAvailable items:")
    for n in range(len(availableTools)):
        print(availableTools[n][0])
    print("\nWhat do you want to use?")
    loop = False
    while currentMove[2] == " ":
        if loop == True:
            print("\nThat is not a vaild item, choose another:")
        loop = True
        do = input(promptText)
        for t in range(len(availableTools)):
            if battleTools[availableTools[t][1]][4] in do.lower():
                currentMove[0] = battleTools[availableTools[t][1]][1] #saves current move [0] to move type
                currentMove[1] = battleTools[availableTools[t][1]][3] #saves current move [1] to move data (how much damage/block)
                currentMove[2] = battleTools[availableTools[t][1]][2] #saves name of move
    if currentMove[0] == 0:
        if currentEnemy[3]-currentMove[1] < 0:
            currentEnemy[1] = currentEnemy[1] + (currentEnemy[3] - currentMove[1])
            currentEnemy[3] = 0
            os.system("cls")
            printBattleStatus()
            print(f"\nYou damage the {currentEnemy[0]} for {-(currentEnemy[3]-currentMove[1])} damage")
        else:
            currentEnemy[3] = currentEnemy[3] - currentMove[1]
            os.system("cls")
            printBattleStatus()
            print(f"\nThe {currentEnemy[0]} blocks your attack")
    elif currentMove[0] == 1:
        player[2] = player[2] + currentMove[1]
        os.system("cls")
        printBattleStatus()
        print(f"\nYou gain {currentMove[1]} block")
    input(waitText)

def enemiesTurn():
    enemyMoves = []
    movePool = []
    currentEnemyMove = [0, 0, " "]
    print(f"\nThe {currentEnemy[0]}'s turn!")
    input(waitText)
    for m in range(currentEnemy[5]):
        enemyMoves.append(currentEnemy[6+m]) #load enemies moves into temp variables
        if (enemyMoves[m][0] == 0) and (enemyMoves[m][1] >= player[0]): #if move is damage, and lethal then add to movepool (if can kill in one hit it will use damage move)
            movePool.append(enemyMoves[m])
    if len(movePool) == 0: #if no moves in pool, will ad every move
        for m in range(len(enemyMoves)):
            movePool.append(enemyMoves[m])
    currentEnemyMove = movePool[random.randint(0, len(movePool)-1)]
    if currentEnemyMove[0] == 0:
        if player[2]-currentEnemyMove[1] < 0:
            player[0] = player[0] + (player[2] - currentEnemyMove[1])
            player[2] = 0
            os.system("cls")
            printBattleStatus()
            print(f"\n{currentEnemyMove[2]} and deals {-(player[2]-currentEnemyMove[1])} damage")
        else:
            currentEnemy[3] = currentEnemy[3] - currentMove[1]
            os.system("cls")
            printBattleStatus()
            print(f"\nYou block the {currentEnemy[0]}'s attack")
    elif currentEnemyMove[0] == 1:
        currentEnemy[3] = currentEnemy[3] + currentEnemyMove[1]
        os.system("cls")
        printBattleStatus()
        print(f"\n{currentEnemyMove[2]} and gains {currentEnemyMove[1]} block")
    input(waitText)
    

def printBattleStatus():
    healthBars = [[], []] #0'th is player, 1'th is enemy's
    for h in range(player[1]-player[0]):
        healthBars[0].insert(0, "□")
    for h in range(player[0]):
        healthBars[0].insert(0, "■")
    for h in range(currentEnemy[2]-currentEnemy[1]):
        healthBars[1].insert(0, "□")
    for h in range(currentEnemy[1]):
        healthBars[1].insert(0, "■")
    print(f"{currentEnemy[0]} health:", end=" ")
    for p in range(len(healthBars[1])):
        print(healthBars[1][p], end=" ")
    print(f"\nYour health:", end=" ")
    for p in range(len(healthBars[0])):
        print(healthBars[0][p], end=" ")
    print("")

def startBattle(enemie): #takes the id of the desired enemie in the enemie list
    global currentEnemy
    currentEnemy = enemies[enemie]
    currentEnemy.insert(len(currentEnemy), currentEnemy[1])
    os.system("cls")
    print(f"An enemy {currentEnemy[0]} attacks!")
    input(waitText)
    while (currentEnemy[1] > 0) and (player[0] > 0 ):
        os.system("cls")
        printBattleStatus()
        time.sleep(0.5)
        playersTurn()
        os.system("cls")
        if currentEnemy[1] > 0:
            printBattleStatus()
            time.sleep(0.5)
            enemiesTurn()
    if player[0] > 0:
        return([True, player[0]])
    else:
        return([False, player[0]])
    
startBattle(0)