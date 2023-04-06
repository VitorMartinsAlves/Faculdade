notas = []
for x in range(3):
    notas.append(float(input("Digite uma nota:")))
print("As notas digitas foram:\n")
for y in range(3):
    print(f"{y+1}º Nota: {notas[y]}")
print(f"Sua média é de {(notas[0]*2+notas[1]*3+notas[2]*5)/10:.1f}")
