def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)

N = int(input())  

for _ in range(N):
    F1, F2 = map(int, input().split())  
    mdc = MDC(F1, F2)  
    print(mdc)