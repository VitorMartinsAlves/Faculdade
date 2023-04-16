side = float(input("Digite o 1º lado: "))
side2 = float(input("Digite o 2º lado: "))
side3 = float(input("Digite o 3º lado: "))
equalSide = 0

if side == side2:
    equalSide += 1
if side == side3:
    equalSide += 1

if equalSide == 1:
    print("Isóscele")
elif equalSide == 2:
    print("Equilátero")
else:
    print("Escaleno")
