import math

while True:
    try:
        N = int(input())
        
        H, C, L = map(int, input().split())
        
        diagonal = math.sqrt(H**2 + C**2)
        
        area_total = N * diagonal * L / 10000
        
        print(f'{area_total:.4f}')
    except EOFError:
        break