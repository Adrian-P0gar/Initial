numbers = []
x= int(input("How many numbers?"))
i = 0
n = 0
while (i < x):
    el = int(input("Elementul" + str (i) + ":"))
    numbers.append(el)
    i = i+1
print(numbers)

c = int(len(numbers))
while (n <= c):

    j = 0
    while j <= c - 2:
        while numbers[j] > numbers[j +1]:
            temp = numbers[j + 1]
            numbers[j +1] = numbers[j]
            numbers[j] =temp
        j = j+1
    n = n+ 1

print(numbers)

