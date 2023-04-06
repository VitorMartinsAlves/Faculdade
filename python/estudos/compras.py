def init(a, b):

    buying(a, b)
    print(a, b)


def buying(a, b):
    chosen = input("Digite o número do produto (para sair aperte 0:")

    if a == "0":
        return 0;
    print(a, b)
    init(a, b)


shop = [("Maça", 12.34), ("Açucar", 23.04), ("Chocolate", 5.99)]
item = 1
print("Escolha quais itens gostaria de colocar na sua cesta:")
for x in shop:
    print(f"Nº {item} - {x[0]} - R$ {x[1]}")
    item = item + 1


buying()
