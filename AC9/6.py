N = int(input())

intervalos = []
for _ in range(N):
    T, V = map(int, input().split())
    intervalos.append((T, V))

distancia_total = sum(T * V for T, V in intervalos)

print(distancia_total)