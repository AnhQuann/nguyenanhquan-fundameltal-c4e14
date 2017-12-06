from random import randint

luck = int(input("Luck: "))
agi = int(input("Agi: "))

dice = randint(0, 6)

if(luck + agi < dice):
    print("Ăn đòn")
else:
    print("Hụt")
