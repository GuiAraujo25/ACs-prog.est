while True:
    n = int(input())
    if n == 0: break

    m = 0
    j = 0

    aux = [int(i) for i in input().split()]

    for i in aux:
        if i == 0:
            m += 1
        else:
            j += 1
    print(f"Mary won {m} times and John won {j} times")            