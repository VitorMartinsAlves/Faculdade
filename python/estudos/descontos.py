def discountFunction(a, b):
    if b > 100 and b < 0:
        return print("Descontos maiores que 100% e menos que 0% são inválidos.")

    return print("O valor do produto com o desconto é de R${:.2f}!".format(
        a - (a * b / 100)))


price = float(input("Digite o valor do produto: R$"))
discount = float(input("Digite o desconto que quer aplicar no produto: "))

discountFunction(price, discount)
