game_dictionary = {'home': {'team_name': 'Brooklyn Nets',
                            'colors': ['Black', 'White'],
                            'players': {'Alan Anderson': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 22,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 1
                                        },
                                        'Reggie Evans': {
                                            'number': 30,
                                            'shoe': 14,
                                            'points': 12,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 12,
                                            'blocks': 12,
                                            'slam_dunks': 7
                                        },
                                        'Brook Lopez': {
                                            'number': 11,
                                            'shoe': 17,
                                            'points': 17,
                                            'rebounds': 19,
                                            'assists': 10,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 15
                                        },
                                        'Mason Plumlee': {
                                            'number': 1,
                                            'shoe': 19,
                                            'points': 26,
                                            'rebounds': 12,
                                            'assists': 6,
                                            'steals': 3,
                                            'blocks': 8,
                                            'slam_dunks': 5
                                        },
                                        'Jason Terry': {
                                            'number': 31,
                                            'shoe': 15,
                                            'points': 19,
                                            'rebounds': 2,
                                            'assists': 2,
                                            'steals': 4,
                                            'blocks': 11,
                                            'slam_dunks': 1
                                        }
                                        }},
                    'away': {'team_name': 'Charlotte Hornets',
                            'colors': ['Turquoise', 'Purple'],
                            'players': {'Jeff Adrien': {
                                            'number': 4,
                                            'shoe': 18,
                                            'points': 10,
                                            'rebounds': 1,
                                            'assists': 1,
                                            'steals': 2,
                                            'blocks': 7,
                                            'slam_dunks': 2
                                        },
                                        'Bismak Biyombo': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 12,
                                            'rebounds': 4,
                                            'assists': 7,
                                            'steals': 7,
                                            'blocks': 15,
                                            'slam_dunks': 10
                                        },
                                        'DeSagna Diop': {
                                            'number': 2,
                                            'shoe': 14,
                                            'points': 24,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 4,
                                            'blocks': 5,
                                            'slam_dunks': 5
                                        },
                                        'Ben Gordon': {
                                            'number': 8,
                                            'shoe': 15,
                                            'points': 33,
                                            'rebounds': 3,
                                            'assists': 2,
                                            'steals': 1,
                                            'blocks': 1,
                                            'slam_dunks': 0
                                        },
                                        'Brendan Haywood': {
                                            'number': 33,
                                            'shoe': 15,
                                            'points': 6,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 22,
                                            'blocks': 5,
                                            'slam_dunks': 12
                                        }}}}


def num_points_scored(name):
    name = name.title()
    for home_away in game_dictionary:
        for player in game_dictionary[home_away]['players']:
            if player == name:
                return game_dictionary[home_away]['players'][name]['points']
        
def shoe_size(name):
    name = name.title()
    for home_away in game_dictionary:
        for player in game_dictionary[home_away]['players']:
            if player == name:
                return game_dictionary[home_away]['players'][name]['shoe']
 
        
def team_colors(name_of_team):
    name_of_team = name_of_team.title()
    for i in game_dictionary:
        if game_dictionary[i]['team_name'] == name_of_team:
            return game_dictionary[i]['colors']

def team_names():
    return [game_dictionary[i]['team_name'] for i in game_dictionary]

def players_numbers(name_of_team):
    name_of_team = name_of_team.title()
    list_of_numbers =[]
    for i in game_dictionary:
        if game_dictionary[i]['team_name'] == name_of_team:
            for player in game_dictionary[i]['players']:
                list_of_numbers.append(game_dictionary[i]['players'][player ['number'])
            return list_of_numbers
                                                                     
def player_stats(name):
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            if x == name:
                return game_dictionary[i]['players'][name]
                                                                     
def big_shoe_rebounds():
    big_shoes = []
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            big_shoes.append(game_dictionary[i]['players'][x]['shoe'])
    shoe_big = max(big_shoes)
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            if game_dictionary[i]['players'][x]['shoe'] == shoe_big:
                return game_dictionary[i]['players'][x]['rebounds']
                                                                     
                                                              
                                                                     
def most_player_points():
    most_points = []
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            most_points.append(game_dictionary[i]['players'][x]['points'])
    leading_scorer = max(most_points)
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            if game_dictionary[i]['players'][x]['points'] == leading_scorer:
                return x
                                                                     
def winning_team():
    home_team_points = sum([game_dictionary['home']['players'][x]['points'] for x in game_dictionary['home']['players']])
    away_team_points = sum([game_dictionary['away']['players'][x]['points'] for x in game_dictionary['away']['players']])
    if home_team_points > away_team_points:
        return game_dictionary['home']['team_name']
    else:
        return game_dictionary['away']['team_name']
                                                                     
                                                                     
def player_with_longest_name():
    names_of_players = []
    length_of_names = []
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            names_of_players.append(x)
    for y in names_of_players:
        length_of_names.append((len(y),y))
    return sorted(length_of_names)[-1]
                                                                     
                                                                                                                                 
def long_name_steals_a_ton():
    names_of_players = []
    for i in game_dictionary:
        for x in game_dictionary[i]['players']:
            names_of_players.append((game_dictionary[i]['players'][x]['steals'],x))
    return player_with_longest_name()[1] == sorted(names_of_players)[-1][1]                                                                     
                                                                     
                                                                     





        


