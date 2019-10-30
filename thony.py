import random
import sys

d = {}
life = 5

file = open('/home/pogar/codecool/test.txt', 'r')

for line in file:
    # print(line)
    (key, val) = [l.strip()for l in line.split(":")]
    d[key] = val
    # print(key)

file.close()

# print(d)

keys = list(d.keys())
randomcountry = keys[random.randint(0, len(keys) - 1)]
capital = list(d[randomcountry])
# print(randomcountry)
print(capital)
print(capital[0], "-" * (len(capital) - 2), capital[-1])
#print(capital[0], "-".join(capital), capital[-1])
# lungime = len(capital)
# alegere = 1
# while alegere < 10:
#     litera = input("Give me a letter:")
#     if not litera in capital:
#         print("You not have this letter in the word!")
#     elif litera in capital:
#         print ()


# while (i < (l - 1)):
#     litera = input("Give me a letter: ")
#     lungimelitera = input(litera)
#     if lungimelitera == 1:
#         if litera == str(capital[i]):
#             print(litera)
print(litera.join(capital))
