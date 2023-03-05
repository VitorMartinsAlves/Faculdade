import os

# tentando usar esta função para criar um "pseudo loop"


def initFunc(storage, hands):
    os.system("cls")
    print("Seu saldo é de R${:.2f}, você tem R${:.2f} em mãos.\n".format(
        storage, hands))
    choice = int(input("1 - Depósitar\n2 - Sacar\n3 - Transferir\nEscolha:"))
    return switchCase(choice, storage, hands)

# tentando elaborar um switch case em python


def switchCase(opt, storage, hands):
    os.system("cls")
    if opt == 1:
        x = float(input("Valor para ser depósitado R$"))
        if x <= hands:
            hands = hands - x
            storage = storage + x
    if opt == 2:
        b = float(input(f"Saldo atual R${storage}\nValor para ser sacado R$"))
        if b <= storage:
            hands = hands + b
            storage = storage - b
    if opt == 0:
        return 0

    return initFunc(storage, hands)


account = 0
storage = 0
hands = 50
initFunc(storage, hands)

# to do
friendAccount = 0
