CurrentFloor = int(0)
CurrentRoom = int(0)

def TowerLobby():
    if GoUp:
        CurrentFloor += 1
    if NextRoom:
        CurrentRoom += 1
