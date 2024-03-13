# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.
def treecoords(tree: dict, current_coord: tuple=()) ->  tuple:  
    coordinates = []  # Coord             
    for key, value in tree.items():      
        if isinstance(value, dict):
         coordinates.extend(treecoords(value, current_coord + (key,)))         
        # Gör ett rekursivt anrop
        else:
    # Hantera värdet som inte är en dictionary
            coordinates.append((current_coord + (key, ),value))
    return tuple(coordinates)   



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


# Här kan du skriva testkod för din funktion. Denna körs endast när du kör
# filen direkt, och inte när du importerar den som modul i en annan fil.
# Koden importeras som en modul av autograding-funktionen för att utföra ett
# "smoke test" av din funktion, så det är viktigt att din kod inte kör något
# utanför denna if-sats.
#
# Exempel:
#
# print(funktionsnamn("hejsan", 99))
# print(funktionsnamn([19, 22, 31, 29, 1])
# Ta bort denna rad


