import time


def groupInfo():
    print("\n\n- Análise e Desenvolvimento de Sistemas\n- Vitor Martins (34333193), Tiago Esteves(7233880930), Ueslei, Alexandre César da silva(32846134)\n- Redes de Computadores e Programação para internet\n- 0.1\n\n")
    time.sleep(10)
# print(groupInfo())


def decimalConvert(value):
    converted_value = list(value)
    acumu = 0
    for x, index in enumerate(converted_value):
        print((int(x)**2)+int(index))

    print(acumu)


print(1*0)
# activeMenu = True
# while activeMenu:
#     print("\n\n1\nMenu:\n1- Dados do grupo e aplicação\n2- Resolução da atividade proposta.")
#     choice = int(input("Digite uma opção: "))
#     if choice == 1:
#         groupInfo()
#     if choice == 2:
#         binarioValue = input(
#             "Digite o valor que quer converter para decimal: ")
#         decimalConvert(binarioValue)
