x = []
n = int(input("Cate elemente are list?"))
i = 0
while (i < n):
    el = int(input("Elementul al" + (str(i) + "-ulea")))
    x.append(el)
    i = i +1

swap = True
while ( swap is True):
    swap = False
    for i in range(0, n - 1):
        if x[i] > x[i +1]:
            aux = x[i]
            x[i] = x[i +1]
            x[i+1] = aux
            swap = True

print (x)