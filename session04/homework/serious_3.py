x = int(input('Enter a number: '))

prime = False

if x != 2:
    for i in range(2, x):
        if x % i == 0 or x <= 1:
            break
        else:
            prime = True
else:
    prime = True

if not prime:
    print("{0} is not a prime number".format(x))
else:
    print("{0} is a prime number".format(x))
