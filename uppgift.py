def treecoords(tree: dict, current_coord: tuple=()) -> tuple: 
    # Funktionen treeecoords läser träd strukturerat data och omvanldar det till en platt lista av tuples. 
    # Varje tuple har en sökväg i trädet.
    results = []  # Skapar en tom lista för att samla ihop alla koordinaterna och värdena.

    for key, value in tree.items(): # Loopar igenom varje element i trädet.
        new_coord = current_coord + (key,) # Skapar en ny koordinat baserad på den aktuella platsen.

        if isinstance(value, dict):
            # Om värdet är en dictionary då finns det mer nivåer att utforska i trädet genom ett rekursivt anrop.
            # Loopen fortsätter tills den når den sista nivån i trädet.
            results.extend(treecoords(value, new_coord))
        else: 
            # Om värdet inte är en dictionary, läggs den nya koordinat och värdet i listan "results".
            results.append((new_coord, value))

    return tuple(results)  # Resultatet returneras som en tuple.

if __name__ == "__main__":

    print(treecoords({
    "a": 1,
    "b": 2
}))
    print(treecoords({
    "x": {
        "y": 3
    },
    "z": 4
}))
    print(treecoords({
    "root": {
        "left": 5,
        "right": {
            "left": 6,
            "right": 7
        }
    }
}))
    print(treecoords({
    "1": {
        "2": {
            "3": {}
        },
        "4": {
            "5": 8,
            "6": 9
        }
    }
}))
    print(treecoords({
    "a": {
        "b": {
            "c": 10,
            "d": 11
        },
        "e": {
            "f": 12
        }
    },
    "g": 13
}))
