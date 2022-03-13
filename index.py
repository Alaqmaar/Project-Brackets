team_details = {}
win_details = {}

number_of_teams = int(input("Enter the nubmer of teams: "))

for i in range(number_of_teams):
    name_of_team = input("Enter the name of the team: ")
    elo_of_team = int(input("Enter the elo of the team: "))

    team_details[name_of_team] = elo_of_team

while True:
    while True:
        team_one = max(team_details)
        one_elo = team_details[team_one]
        del team_details[team_one]

        team_two = max(team_details)
        two_elo = team_details[team_two]
        del team_details[team_two]

        winning_team = input("Enter the name of the winning team: ")
        
        if winning_team == team_one:
            win_details[team_one] = one_elo
        elif winning_team == team_two:
            win_details[team_two] = two_elo

        