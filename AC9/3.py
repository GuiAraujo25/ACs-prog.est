N = int(input())

for _ in range(N):
    M = int(input())
    preco = {}

    for _ in range(M):
        fruta, p = input().strip().split(" ")
        preco[fruta] = float(p)

    P = int(input())

    resposta = 0.0
    for _ in range(P):
        fruta, quantidade = input().strip().split(' ')
        resposta += int(quantidade) * preco[fruta]

    print(f'R$ {resposta:.2f}')