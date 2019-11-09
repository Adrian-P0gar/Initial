import random
import sys

d = {}
life = 5

file = open('/home/pogar/codecool/test.txt', 'r')

for line in file:
    # print(line)
    (key, val) = line.split(":", 1)
    d[key] = val
    # print(key)

file.close()

# print(d)

keys = list(d.keys())
randomcountry = keys[random.randint(0, len(keys)-1)]

# print(randomcountry)

capital = d[randomcountry]

print(capital)

l = len(capital)-1
# print(l)

guess = [capital[0]]
d = 1

for d in range(1, l-1):
    guess.insert(d, ' -')
    d += 1

guess.extend(capital[l-1])
#print(capital[0], (l-2) * '_ ', capital[l-1])
print(guess)


a = input("Press l for letter or w for word: ")
i = 1

if a == "l":
    while (i < (l-1)):
        k = input("Please give me a letter: ")
        j = len(k)
        if j == 1:
            if k == str(capital[i]):
                print(k)
                guess[i] = k
                print(guess)
            print(" ".join(guess))
        i += 1
