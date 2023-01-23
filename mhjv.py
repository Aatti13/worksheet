def teams(x, y):
    d = {}
    team_leaders = [i+1 for i in range(y)]
    team_members = [_+x+1 for _ in range(y-x)]
    for i in range(x):
        if len(team_members) % x > i:
            d[team_leaders[i]] = team_members[i * (len(team_members) // x + 1):(i + 1) * (len(team_members) // x + 1)]
        else:
            d[team_leaders[i]] = team_members[i * (len(team_members) // x) +
                                              (x - i - 1):(i + 1) * (len(team_members) // x) + (x - i - 1)]
    return d


a = int(input("Enter number of members: "))
b = int(input("Enter number of leaders: "))