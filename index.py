# Project Brackets
# Create a Tournament Management System

# First team to 13 points wins the game

a = 0
b = 0

print('Type \'A\' to add a point to Team A.')
print('Type \'B\' to add a point to Team B.')

while a < 13 and b < 13:
    pt = input()

    if pt == 'A':
        a += 1
    elif pt == 'B':
        b += 1
    else:
        print('Invalid Input')
        continue

    print('Team A:', a)
    print('Team B:', b)

if a == 13:
    print('Team A Wins!')
else:
    print('Team B Wins!')
