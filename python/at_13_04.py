condi = True
condi2 = True
condi3 = 10
condi4 = True
Soma = 0
if condi:
    print(f"Condição 01 {type(condi),condi}")
elif condi2:
    print(f"Condição 02 {type(condi2),condi2}")
    Soma = "2"+"2"
else:
    print(f"Condição 02 {type(condi2),condi2}")

print(Soma)
print(10*'/')

Soma = 2+2
print(Soma)
print('/n')

if condi4:
    print(f"Palmeiras 8 vezes campeão paulista")
    Soma = 2+2
else:
    print(f"Agua santa é de DIADEMA")

if condi3 >= 10:
    print(f'N <=10 {condi3}')
    x = input("Digite seu nome: ")
    print(x)
elif condi3 >= 11:
     print(f'N <=11 {condi3}')
     x = input("Digite seu Sobrenome: ")
     print(x)
else: 
    print(f'N >=12 {condi3}')
    x = input("Digite seu TIME: ")
    print(x)