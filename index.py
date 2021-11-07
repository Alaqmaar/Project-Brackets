# Team Registration

nTeams = int(input('Enter the number of participating teams: '))
teams = []
elo = []
round = []
eround = []

print()

for i in range(0, nTeams):
    teams += [input('Enter the name of Team: ')]
    elo += [int(input('Enter the teams elo (If the team is not rated, enter 0): '))]
    print()

if len(teams) % 2 != 0:
    round += [teams[elo.index(max(elo))]]
    eround += [max(elo)]

    print(max(elo))
    teams.remove(teams[elo.index(max(elo))])
    elo.remove(max(elo))

i = 1

while len(teams) > 1:
    t1 = teams[elo.index(max(elo))]
    e1 = max(elo)

    teams.remove(t1)
    elo.remove(max(elo))

    t2 = teams[elo.index(max(elo))]
    e2 = max(elo)

    teams.remove(t2)
    elo.remove(max(elo))

    print('Match', str(i) + ':', t1, 'vs', t2)

    i += 1

    win = input('Enter the name of the winning team: ')

    if t1.startswith(win):
        round += [t1]
        eround += [e1]
    else:
        round += [t2]
        eround += [e2]

print(round)
print(eround)

# Winning criteria

print()

if len(teams) == 1:
    print(teams[0], 'has won the tournament!')
