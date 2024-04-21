qntd_pares = 0

for _ in range(5):
    valor = int(input("Digite um valor inteiro: "))
    if valor % 2 == 0:
        qntd_pares += 1

print("valores pares", qntd_pares)