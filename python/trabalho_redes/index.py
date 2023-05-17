import time
def groupInfo():
    return "\n\n- Análise e Desenvolvimento de Sistemas\n- Vitor Martins (34333193), Tiago Esteves(7233880930), Ueslei (33459878), Alexandre César da silva(32846134)\n- Redes de Computadores e Programação para internet\n- 0.1\n\n"

def convert_bi(binario):
    decimal = 0
    potencia = 0
    while binario != 0:
        digito = binario % 10
        decimal += digito * (2 ** potencia)
        binario //= 10
        potencia += 1
    return decimal

activeMenu = True
while activeMenu:
    print("\n\n\nMenu:\n1- Dados do grupo e aplicação\n2- Resolução da atividade proposta.")
    choice = int(input("Digite uma opção: "))
    if choice == 1:
        print(groupInfo())
        time.sleep(10)
    if choice == 2:
        converted = convert_bi(int(input("Digite um valor para ser convertido para decimal: ")))
        print(f"O valor convetido é : {converted}")
        time.sleep(10)
