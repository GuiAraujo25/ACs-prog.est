x = int(input())
y = int(input())

s = 0

if x > y: 
    x,y = y,x 

for elemento in range(x, y+1):
    if elemento % 13 != 0:
        s += elemento
print(s)
