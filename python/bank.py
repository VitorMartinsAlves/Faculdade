import os

# using this function to make a "pseudo loop"


def initFunc(storage, hands):
    os.system("cls")
    print("Seu saldo é de R${:.2f}, você tem R${:.2f} em mãos.\n".format(
        storage, hands))
    choice = int(input("1 - Depósitar\n2 - Sacar\n3 - Transferir\nEscolha:"))
    return switchCase(choice, storage, hands)

# trying to make switch case on python


def switchCase(opt, storage, hands):
    if opt == 1:
        os.system("cls")
        x = float(input("Valor para ser depósitado R$"))
        if x > hands:
            return initFunc(storage, hands)
        hands = hands - x
        storage = storage + x
        return initFunc(storage, hands)
    if opt == 2:
        os.system("cls")
        x = float(input("Valor para ser sacado R$"))
        if x > storage:
            return initFunc(storage, hands)
        hands = hands + x
        storage = storage - x
        return initFunc(storage, hands)
    if opt == 0:
        return 0


account = 0
storage = 0
hands = 50
initFunc(storage, hands)

# to do
friendAccount = 0
