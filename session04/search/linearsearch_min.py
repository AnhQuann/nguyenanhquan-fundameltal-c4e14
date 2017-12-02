numbers = [5, 2, 3, 9, 4]

Min = numbers[0]

# for i in range(len(numbers)):
#     for j in range(1, len(numbers)-1):
#         if numbers[i] < numbers[j]:
#             j+=1
#         else:
#             Min = numbers[j]
#
# print(numbers[j])

for num in numbers:
    if Min > num:
        Min = num

print(Min)
