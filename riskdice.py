import random

def unu_cu_unu():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    c = random.randrange(1,7)
    d = random.randrange(1,7)
    e = random.randrange(1,7)
    print("Attacker Dice:", a, "\n" "Defender Dice:", d)
    Def = (2)
    Atk = (3)
 
    if a >= d:
        Def = (Def - 1)
    elif a == d:
        Atk = (Atk - 1)   
    else:
        Atk = (Atk - 1)

    if Atk == 3:
        print("Ataker: Lost 0 units")
    elif Atk == 2:
        print("Ataker: Lost 1 units")
    elif Atk == 1:
        print("Ataker: Lost 2 units")

    if Def == 2:
        print('Defender: Lost 0 unist')
    elif Def == 1:
        print('Defender: Lost 1 unist')
    elif Def == 0:
        print('Defender: Lost 2 unist')

    return


z = input("How many units attack:")
k = input ("How many units defend:")
if z == ("1") and k == ("1"):
    unu_cu_unu()
else:
    print("nu")




   