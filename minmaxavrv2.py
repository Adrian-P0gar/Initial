numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
n = len(numbers)
def maximum():
    maxi = numbers[0]
    i = 1
    n = len(numbers)
    while i < n:
        if numbers[i] > maxi:
            maxi = numbers[i]
        
        i = i + 1

    return maxi
    

    

def minimum():

    mini = numbers[0]
    i = 1
    n = len(numbers)
    while i < n:
        if numbers[i] < mini:
            mini = numbers[i]
        
        i = i+1

    return mini

print(maximum())
print(minimum())

suma = 0

for num in numbers:
    suma= suma + int(num)

print(suma/ n)
