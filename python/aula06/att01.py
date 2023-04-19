def at01():
    side = float(input("Digite o 1º lado: "))
    side2 = float(input("Digite o 2º lado: "))
    side3 = float(input("Digite o 3º lado: "))
    equalSide = 0

    if side == side2:
        equalSide += 1
    if side == side3:
        equalSide += 1
    if equalSide == 1:
        return "Isóscele"
    elif equalSide == 2:
        return "Equilátero"
    else:
        return "Escaleno"
def at02():
    sides = int(input("Quantidade de lados: "))

    # atividade 04
    if sides < 3:
        return "Não é um polígono"
    if sides == 3:
        side01 = float(input("Digite o 1º lado: "))
        side02 = float(input("Digite o 2º lado: "))
        triArea = (side01*side02)/2
        return f"\nO triângulo tem {triArea:.1f} m²"
    if sides == 4:
        side01 = float(input("Digite o 1º lado: "))
        side02 = float(input("Digite o 2º lado: "))
        quadArea = side01*side02
        return f"O quadrado tem {quadArea} m²"
    if sides == 5:
        side01 = float(input("Digite um lado do pentâgono lado: "))
        apotema = float(input("Digite o tamanho do apótema: "))
        pentArea = ((side01*5)/2) * apotema
        return f"O pentâgono tem {pentArea} m²"

    # atividade 04
    if sides > 5:
        return "Polígono não identificado"
def at03():
    height = float(input("Digite sua altura em metros: "))
    gender = int(
        input("Digite seu sexo (1 para feminino e 2 para masculino): "))
    if gender == 1:
        idealWeight = (62.1 * height) - 44.7
    elif gender == 2:
        idealWeight = (72.7 * height) - 58
    else:
        return "Sexo inválido! Por favor, digite 1 para feminino ou 2 para masculino."
        # exit()

    return "Seu peso ideal é de {:.1f} kg.".format(idealWeight)
def at05():
    angle1 = float(input("Digite o valor do primeiro ângulo: "))
    angle2 = float(input("Digite o valor do segundo ângulo: "))
    angle3 = float(input("Digite o valor do terceiro ângulo: "))

    soma_angles = angle1 + angle2 + angle3
    if soma_angles == 180:
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            return "O triângulo é Retângulo."
        elif angle1 > 90 or angle2 > 90 or angle3 > 90:
            return "O triângulo é Obtusângulo."
        else:
            return "O triângulo é Acutângulo."
    else:
        return "Os valores informados não correspondem a um triângulo."

print(at02())