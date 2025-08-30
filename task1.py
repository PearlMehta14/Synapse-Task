from itertools import combinations


pokedex = {
    'Pikachu': ('Electric',),
    'Charizard': ('Fire', 'Flying'),
    'Lapras': ('Water', 'Ice'),
    'Machamp': ('Fighting',),
    'Mewtwo': ('Psychic', 'Fighting'),
    'Hoopa': ('Psychic', 'Ghost', 'Dark'),
    'Lugia': ('Psychic', 'Flying', 'Water'),
    'Squirtle': ('Water',),
    'Gengar': ('Ghost', 'Poison'),
    'Onix': ('Rock', 'Ground'),
}

k=int(input("Enter K:"))

best = []
max = 0

for team in combinations(pokedex.keys(), k):
    types = set()
    for p in team:
        types.update(pokedex[p])
    if len(types) > max:
        max = len(types)
        best = [(team, types)]
    elif len(types) == max:
        best.append((team, types))

print("Max distinct types:", max)
for team, types in best:
    print(team, "-->", types)
