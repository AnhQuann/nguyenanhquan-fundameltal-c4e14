menu = ['death note', 'netflix', 'teaching']
print('Hi there, here your favorite things so far ', *menu, sep=',')
# print(*menu, sep=',')
name = input(('One thing you want to add? '))
menu.append(name)
print(*menu, sep=', ')
