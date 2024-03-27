# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.
def treecoords(tree: dict, current_coord: tuple=()) -> tuple: 
    list=[]
    for key, value in tree.items():
        new_coord=current_coord+(key,)
        if isinstance(value , dict):
            list.extend(treecoords(value, new_coord))
        else:
            list.append((new_coord, value))
    return tuple(list)
    #print(current_coord + (f"Key:{key}, Value: {value}"))


if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #print(treecoords({ "a": 1, "b": 2 }))
    #print(treecoords({ "x": { "y": 3 }, "z": 4 }))
    print(treecoords({ "root": {"left": 5, "right": { "left": 6, "right": 7 } } } ))
    
    treecoords({ "a": {"b": {"c": 10,"d": 11 },"e": { "f": 12 } } ,"g": 13 } )
    
