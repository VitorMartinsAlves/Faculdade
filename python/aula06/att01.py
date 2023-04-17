# atividade 01
def at01():
    side = float(input("Digite o 1º lado: "))
    side2 = float(input("Digite o 2º lado: "))
    side3 = float(input("Digite o 3º lado: "))
    equalSide = 0

    if side == side2:
        # dois lados iguais
        equalSide += 1
    if side == side3:
        # tres lados iguais
        equalSide += 1

    if equalSide == 1:
        return "Isóscele"
    elif equalSide == 2:
        return "Equilátero"
    else:
        return "Escaleno"
# print(at01())
# atividade 02


def at02():
    sides = int(input("Quantidade de lados: "))

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


print(at02())
