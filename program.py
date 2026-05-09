boardGame = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
isGameOver = False

def printBoard():
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(boardGame[i][j], end=" ")
        print()

def checkHorizontalWin():
    for i in range(3):
        if boardGame[i][0] == boardGame[i][1] == boardGame[i][2] != '-':
            return True
    return False

def checkVerticalWin():
    for j in range(3):
        if boardGame[0][j] == boardGame[1][j] == boardGame[2][j] != '-':
            return True
    return False

def checkDiagonalWin():
    if boardGame[0][0] == boardGame[1][1] == boardGame[2][2] != '-':
        return True
    if boardGame[0][2] == boardGame[1][1] == boardGame[2][0] != '-':
        return True
    return False

def checkWin():
    if checkHorizontalWin() or checkVerticalWin() or checkDiagonalWin():
        return True
    return False

def checkDraw():
    for i in range(3):
        for j in range(3):
            if boardGame[i][j] == '-':
                return False
    return True

def isValidMove(x, y):
    return 0 <= x < 3 and 0 <= y < 3

print("Bem-vindo ao jogo da velha")
jogador1 = input("Digite o nome do jogador 1 (X): ")
jogador2 = input("Digite o nome do jogador 2 (Y): ")
jogadorDaVez = jogador1

while not isGameOver:
    printBoard()

    coordenadaX = int(input(f"{jogadorDaVez} (jogador X), digite a coordenada X (0-2): "))
    coordenadaY = int(input(f"{jogadorDaVez} (jogador Y), digite a coordenada Y (0-2): "))

    if isValidMove(coordenadaX, coordenadaY) == False:
        print("Coordenadas inválidas. Tente novamente.")
        continue

    if boardGame[coordenadaX][coordenadaY] == '-':
        boardGame[coordenadaX][coordenadaY] = 'X' if jogadorDaVez == jogador1 else 'Y'
        if checkWin():
            printBoard()
            print(f"{jogadorDaVez} venceu!")
            isGameOver = True
        elif checkDraw():
            printBoard()
            print("Empate!")
            isGameOver = True
        else:
            jogadorDaVez = jogador2 if jogadorDaVez == jogador1 else jogador1
    else:
        print("Essa posição já está ocupada. Tente novamente.")
        