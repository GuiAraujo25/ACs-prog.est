N = int(input())

for _ in range(N):
    C = float(input())

    numero = 0
    while (C > 1.0):
        numero += 1
        C /= 2

    print(f'{numero} dias')