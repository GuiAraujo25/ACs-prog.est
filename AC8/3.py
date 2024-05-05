import sys
import math

for line in sys.stdin:
    M, N = map(int, line.strip().split())

    if M == -1 and N == -1:  
        break

    soma_fatoriais = math.factorial(M) + math.factorial(N)
    print(soma_fatoriais)