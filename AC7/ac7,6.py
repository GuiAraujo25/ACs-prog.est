C = int(input())
T = input()

M = []
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    M.append(linha)

soma = 0
elementos = 0
for i in range(12):
    soma += M[i][C]
    elementos += 1

resultado = soma / elementos if T == 'M' else soma

print("{:.1f}".format(resultado))