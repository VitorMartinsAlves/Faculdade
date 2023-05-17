def groupInfo():
    return "Turma: 1i\nIntegrantes do grupo:\n- Vitor Martins Alves\n- Tiago Esteves Albano (7233880930)\n- Ueslei "

print(groupInfo())

activeMenu = True
while activeMenu:
    print("Menu:\n1- Dados do grupo\n2- Resolução da atividade proposta  ")
    choice = int(input("Digite uma opção: "))