T = int(input())

Acertos = 0

a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])
    if a[i] == T:
        Acertos = Acertos = 1

print(Acertos)        