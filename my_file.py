numbers =[56, 2, 54, 3, 1, 6 , 10]
print(numbers)
i = 1
n = len(numbers)




while (i <= n):

    j= 0
    while j<= n - 2:
        while numbers[j] > numbers[j + 1]:
            temp = numbers[j +1]
            numbers[j +1] =numbers[j]
            numbers[j] = temp

        j = j +1
    
    i = i +1

print(numbers)