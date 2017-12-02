bacteriaB = int(input('How many B bacteria are there? '))
minute = int(input('How much time in minute will we wait? '))

looptime = int(minute/2)

for i in range(looptime):
    bacteriaB=bacteriaB*2

print('After {0} minutes, we would have {1} bacterias'.format(minute, bacteriaB))
