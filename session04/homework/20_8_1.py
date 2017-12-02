text = input("Enter a sentence: ")
newtext = text.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = {}

for i in newtext:
    if i in alphabet:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

for j in count:
    print(j, count[j])
