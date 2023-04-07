# ex 1
data = int(input("Digite um número:"))
if data > 10:
    print(f"O valor digitado é maior que 10")
else:
    if data == 10:
        print(f"O valor digitado é igual a 10")
    else:
        print(f"O valor digitado é menor a 10")
# ex 2
x = float(input("Digite seu sálario"))
y = float(input("Digite seus gastos"))
if y > x:
    print(f"Estourou o orçamento")
else:
    print("Gastos dentro do orçamento")
# ex 3
a = float(input("Digite um numero"))
b = float(input("Digite outro numero"))

if a == b:
    print("Estes numeros são iguais")
else:
    print("Estes números são iguais")

# ex 4
z = float(input("Digite um numero"))
y = float(input("Digite outro numero"))

if z > y:
    print(f"O valor {z} é maior que {y}")
else:
    if y > z:
        print(f"O valor {y} é maior que {z}")

# ex 5
k = float(input("Digite um numero"))
l = float(input("Digite outro numero"))
if k > l:
    print(f"{l,k}")
else:
    if k < l:
        print(f"{k}")

# ex 6
idade = float(input("Digite seu ano de nascimento"))
idade = idade - 2023
if idade > 16:
    print("Você pode votar!")
else:
    print("Você não pode votar")

# ex 7
delta = float(input("Digite a quantidade de gols do 1º time"))
lapa = float(input("Digite outro numero"))
if delta > lapa:
    print("O primeiro time ganhou")
else:
    if delta < lapa:
        print("O segundo time ganhou")
    else:
        print("Os dois empataram")

# ex 8
senha = input("Digite sua senha:")
if senha == "123":
    print("Acesso permitido")
else:
    print("Acesso negado")

# ex 9
numMacas = int(input("Digite o número de maças: "))
valor = 0 
print(f" O número de maças é {numMacas}")
if numMacas < 12:
    valor = numMacas * 0.30
else:
    valor = numMacas*0.25
print(f"O valor total da compra é {valor:.2f}")
