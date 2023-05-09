# atividade 01
frase = input("Digite um frase com mais de 3 palavras:")
palavras = frase.split(" ")
for x in palavras:
    print(x)
# atividade 02
inteiro = int(input("Digite um número inteiro positivo: "))
for y in range(1, inteiro+1):
    print(y)
# atividade 03
roof = int(input("Digite quantos números deseja somar:"))
somar = 0
for x in range(0, roof):
    somar += int(input("Digite um número: "))

print(f"A soma total dos números que você digitou é {somar}!")
# atividade 04
phrases = input("Digite um frase consideralvemente grande: ")
words = phrases.split(" ")
typeA = 0
typeB = None
for letters in words:
    if len(letters) > typeA:
        typeA = len(letters)
        typeB = letters

print(f'\n\nA maior palavra que você digitou foi "{typeB}"')
# atividade 05
countV = {'a', 'e', 'i', 'o', 'u'}
phobes = input("Digite uma palavra: ")
counter = 0
for x in countV:
    reducer = phobes.split(x)
    counter += (len(reducer) - 1)
print(f"\nA quantidade de vagais nesta palavra/frase é {counter}.")
# atividade 06
x = int(input("Digite um número: "))
for y in range(11):
    print("{} X {} = {}".format(x, y, x*y))
# atividade 07
palavra = input("Digite uma palavra: ")
reverse = palavra[::-1]
print(reverse)
# atividade 08
number = int(input("Digite um número inteiro positivo: "))
if number > 1:
    i = 2
    while i <= (number // 2):
        if number % i == 0:
            print(number, "não é primo.")
            break
        i += 1
    else:
        print(number, "é primo.")
else:
    print(number, "não é primo.")
# atividade 09
tnumbers = []
while True:
    numero = input("Digite um número (ou 'fim' para parar): ")
    if numero == "fim":
        break
    tnumbers.append(float(numero))
maior = tnumbers[0]
menor = tnumbers[0]
i = 1
while i < len(tnumbers):
    if tnumbers[i] > maior:
        maior = tnumbers[i]
    if tnumbers[i] < menor:
        menor = tnumbers[i]
    i += 1
print("O maior número é:", maior)
print("O menor número é:", menor)
# atividade 10
lista1 = []
numbersx = int(input("Digite o número de elementos da lista 1: "))
for i in range(numbersx):
    numero = float(input("Digite o número {}: ".format(i+1)))
    lista1.append(numero)
lista2 = []
m = int(input("Digite o número de elementos da lista 2: "))
for i in range(m):
    numero = float(input("Digite o número {}: ".format(i+1)))
    lista2.append(numero)
lista_resultante = []
for numero in lista1:
    lista_resultante.append(numero)
for numero in lista2:
    lista_resultante.append(numero)
print("A lista resultante da concatenação é:", lista_resultante)
