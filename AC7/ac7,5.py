N = int(input())

if 1 < N < 1000:

  X = list(map(int, input().split()))

  menor_valor = X[0]
  posicao = 0
  for i in range(1, N):
    if X[i] < menor_valor:
        menor_valor = X[i]
        posicao = i

  print("Menor valor:", menor_valor)
  print("Posicao:", posicao)

else:
  print("Valor inválido")