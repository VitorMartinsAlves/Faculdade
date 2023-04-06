letters = ["a", "e", "i", "o", "u"]
string = "joelho"
count = 0
for x in string:
    for b in letters:
        if x == b:
            count += 1

print(f"Número de vogais: {count}")

value = float(input("value: "))


def parImpar(x):
    if x % 2 == 0:
        print("par")
        return
    print("impar")


parImpar(value)
