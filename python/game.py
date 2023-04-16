import os
import random

square = [
    '⬜', '⬜', '⬜',
    '⬜', '⬜', '⬜',
    '⬜', '⬜', '⬜',
]

win = [
    # horizontal
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    # vertical
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    # diagonal
    (0, 4, 8),
    (2, 4, 6),
]


def showData():
    print(f"{square[0]} | {square[1]} | {square[2]}")
    print(f"{square[3]} | {square[4]} | {square[5]}")
    print(f"{square[6]} | {square[7]} | {square[8]}")


showData()


def verifyWin():
    for x in win:
        # print("combinações")
        # print(x[0], x[1], x[2])
        # print(square[x[0]], square[x[1]], square[x[2]])
        if square[x[0]] == "🟥" and square[x[1]] == "🟥" and square[x[2]] == "🟥":
            print("Vermelho ganhou")
            return True
        if square[x[0]] == "🟦" and square[x[1]] == "🟦" and square[x[2]] == "🟦":
            print("Azul ganhou")
            return True


def botPlay():
    select = False
    count = 1
    for x in range(9):
        if square[x - 1] == "⬜":
            count = count + 1
    if count - 2 == 0:
        print("O jogo acabou!\nNão há mais espaços para selecionar!")
        return

    while not select:
        campo = int(random.randint(1, 9))
        if square[campo - 1] == "⬜" and not square[campo - 1] == "🟥":
            square.pop(campo - 1)
            square.insert(campo - 1, "🟦")
            select = True


def game():
    newPos = int(input("Escolha um quadrado para ocupar (1 a 9): "))
    arrayPos = newPos - 1

    if newPos > 9:
        print("Este campo não existe!")
        return init()

    if square[arrayPos] == "🟥" or square[arrayPos] == "🟦":
        print("Este campo já foi selecionado!")
        return init()

    # print(f"Nova posição {arrayPos}")
    square.pop(arrayPos)
    square.insert(arrayPos, "🟥")

    botPlay()
    showData()
    if verifyWin():
        return print("O jogo acabou!")
    return init()


def init():
    game()


init()
