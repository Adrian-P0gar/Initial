import math
x = 100
y = 999
n = 9
c = []

for i in range(x,y+1):
    if (i%n == 0):
        c.append(i)

print (c[:30])