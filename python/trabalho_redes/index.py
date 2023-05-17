import time


def groupInfo():
    print("- Análise e Desenvolvimento de Sistemas\n- Vitor Martins (34333193), Tiago Esteves(7233880930), Ueslei, Alexandre César da silva(32846134)\n- Redes de Computadores e Programação para internet\n- 0.1")
    time.sleep(10)
# print(groupInfo())


activeMenu = True
while activeMenu:
    print("Menu:\n1- Dados do grupo e aplicação\n2- Resolução da atividade proposta.")
    choice = int(input("Digite uma opção: "))
    if choice == 1:
        groupInfo()
