numbers = [19, 5, 96, 79, 6, 51, 80, 8]

hi = len(numbers)
lo = 0
found = False

x = int(input("Nhap so:"))
while hi>lo:
    mid = (hi+lo)//2
    num = numbers[mid]
    if x == num:
        found = True
        print("Found")
        break
    elif x < num:
        hi = mid
        print('Left')
    else:
        lo = mid+1
        print('Right')

# while x>num:
#     lo = mid
#     if x == mid:
#         found = True
#         break
#
# while x < num:
#     hi = mid + 1
#     if x == mid:
#         found = True
#         break
#
# if not found:
#     print("Not Found")
# else:
#     print('Found!')
