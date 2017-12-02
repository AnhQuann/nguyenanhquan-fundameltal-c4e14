numbers = [19, 5, 96, 79, 6, 51, 80]


# x = int(input("Nhap so: "))
# for i in range(len(numbers)):
#     if x == numbers[i]:
#         print('')

x = int(input("Nhap so: "))

found = False
found_index = -1
#find_first
for index, num in enumerate(numbers):
    if num == x:
        found_index = index
        found = True
        break

if not found:
    print("Not found")
else:
    print('Found {0} at {1}'.format(x, found_index))
