# Funktionen treecords tar två argument, tree som är en dictionary och currenct_cord som är en tuple med kordinater.
# Resultat är en tom lista.
# Funktionen går sedan igenom varje key-value i dictinaryn tree.
# För varje key skapas en ny tuple (new_coord) och den lägger till nyckeln till "current_coord".
# Om värdet (value) för den aktuella nyckeln(Key) är en ordbok, så anropas treecords igen (rekursivt, självupprepande, not to self) och då med new_coord som arg.
# Resultatet av detta läggs till i resultat-listan.
# Om värdet(value) inte är en dictionary så läggs en tuple med nyckeln och värdet till i resultat-listan.
# När hela if-satsen gåtts igenom så returneras listan resultat som en tuple(flera koordinater i detta fall).


def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    resultat = []

    for key, value in tree.items():
        new_coord = current_coord + (key,)

        if isinstance(value, dict):
            resultat.extend(treecoords(value, new_coord))
        else:
            resultat.append((new_coord, value))

    return tuple(resultat)


exempel1 = {"a": 1, "b": 2}

exempel2 = {"x": {"y": 3}, "z": 4}

exempel3 = {"root": {"left": 5, "right": {"left": 6, "right": 7}}}

exempel4 = {"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}

exempel5 = {"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}

print(treecoords(exempel1))
print(treecoords(exempel2))
print(treecoords(exempel3))
print(treecoords(exempel4))
print(treecoords(exempel5))
