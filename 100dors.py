

# doors = [i * 0 for i in range(100)]
# doors = [0] * 100
# index = []
# for c in range(1, 101):
#     for i in range(0, 100, c):
#         if doors[i] == 0:
#             doors[i] = 1
#         else:
#             doors[i] = 0

# for i in range(100):
#     if doors[i] == 1:
#         index.append(i)
# print(doors)

# print(index)

doors = [0] * 100
index = []
x = 1
while x < 100:
    for i in range(0, 100, x):
        if doors[i] == 0:
            doors[i] = 1
        else:
            doors[i] = 0
    x += 1
for i in range(100):
    if doors[i] == 1:
        index.append(i)

print(index)
