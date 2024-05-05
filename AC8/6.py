import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())  

for _ in range(N):
    X = int(input()) 
    if is_prime(X):
        print(f'Prime')
    else:
        print(f'Not Prime')