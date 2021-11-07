nTeams = int(input('Enter the number of participating teams: '))
teams = []
elo = []
pairs = []
epairs = []

print()

for i in range(0, nTeams):
    teams += [input('Enter the name of Team: ')]
    elo += [int(input('Enter the teams elo (If the team is not rated, enter 0): '))]
    print()

if len(teams) % 2 != 0:
    pairs += [teams[elo.index(max(elo))]]
    epairs += [max(elo)]

    print(max(elo))
    teams.remove(teams[elo.index(max(elo))])
    elo.remove(max(elo))

i = 1

while len(teams) > 1:
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
            pairs += [t1]
            epairs += [e1]
        else:
            pairs += [t2]
            epairs += [e2]

    print(pairs)
    print(epairs)

    teams = pairs
    elo = epairs

print()

if len(epairs) == 1:
    print(teams[0], 'has won the tournament!')
