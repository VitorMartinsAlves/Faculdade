# Exercício 1
notas = []
for x in range(3):
    notas.append(float(input(f"Digite a {x+1}º nota: ")))
print("As notas digitas foram:\n")
for y in range(3):
    print(f"{y + 1}º Nota: {notas[y]}")
print(f"Sua média é de {(notas[0] * 2 + notas[1] * 3 + notas[2] * 5) / 10:.1f}\n\n")

# Exercício 2
inputs = []
text = ["Digite suas horas trabalhadas no mês", "Digite o valor da hora trabalhada", "Digite o percentual de desconto"]
for x in range(3):
    inputs.append(float(input(f"{text[x]}: ")))
print(f"Horas Trabalhadas: {inputs[0]}\nSalário Bruto: {inputs[0] * inputs[1]:.2f}\nTotal de Desconto: {(inputs[2] / 100) * (inputs[0] * inputs[1]):.2f}\nSalário líquido: {(inputs[0] * inputs[1]) - (inputs[2] / 100) * (inputs[0] * inputs[1]):.2f}\n\n")

# Exercício 3
F = float(input("Digite a temperatura em graus Fahrenheit: "))
print(f"A temperatura de {F}°F é igual a {(F - 32) / 1.8:.1f}°C\n\n")

# Exercício 4
math = []
for x in range(2):
    math.append(float(input(f"Digite o {x+1}º valor: ")))
print(f"O quadrado da soma dos valores de {math[0]} e {math[1]} é igual a {(math[0]+math[1])**2}")

# Exercício 5
# a) i = (((108)+3) x 9)
#    i = ((80+3) x 9)
#    i = 83 x 9
#    i = 747

# b) j = ((-12) x (-4))+(3 x (-4))
#    j = 48 - 12
#    j = 36
