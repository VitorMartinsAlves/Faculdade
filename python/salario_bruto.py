inputs = []
text = ["Digite suas horas trabalhadas no mês", "Digite o valor da hora trabalhada", "Digite o percentual de desconto"]
for x in range(3):
    inputs.append(float(input(f"{text[x]}: ")))

print(f"Horas Trabalhadas: {inputs[0]}\nSalário Bruto: {inputs[0]*inputs[1]:.2f}\nTotal de Desconto: {(inputs[2]/100)*(inputs[0]*inputs[1]):.2f}\nSalário líquido: {(inputs[0]*inputs[1])-(inputs[2]/100)*(inputs[0]*inputs[1]):.2f}")
