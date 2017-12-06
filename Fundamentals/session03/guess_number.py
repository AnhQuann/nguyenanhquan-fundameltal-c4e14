from random import randint
number = randint(0,100)
guess_wrong = True

# while guess_wrong:
#     i = int(input("Nhap so: "))
#     if i>number:
#         print("Too large!")
#     elif i<number:
#         print("Too small!")
#     else:
#         print("Bingo!")
#         guess_wrong = False

count = 0
while True:

    i = int(input("Nhap so: "))
    count +=1
    if i>number:
        print("Too large!")
    elif i<number:
        print("Too small!")
    else:
        print("Bingo!")
        break
