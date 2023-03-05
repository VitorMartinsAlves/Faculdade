# elaborar uma função que faz o parcelamento e o juros com base no valor repassado pelo usuário
price = float(input("Digite o valor do produto: R$"))
parcelado = int(input("Quer parcelar esta compra em quantas vezes?\n"))

# valor do juros em 0.99
print("O valor da compra ficou parcelado em {} vezes de R${:.2f}".format(
    parcelado, ((price/parcelado)+price * 0.99/100)))
