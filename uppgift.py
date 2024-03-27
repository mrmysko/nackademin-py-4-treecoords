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



# Har start_pos som en tom tuple, för att sedan kunna sammanfoga alla tuplar till en "väg"/tuple som går till värdet
def treecoords(tree_dict, start_pos=()):
    # lista som ska lagra vägen till värdet från start till slut
    slut_pos = []

    # ska gå igenom hela dictionaryn/trädet
    # omvandlar dictionary till tuple par (key:value)
    for key, value in tree_dict.items():
        # lägg till väg/key som den behövt gå från start pos, key är befintlig
        nuvarande_pos = start_pos + (key,)

        # kollar om value är en dictionary eller inte
        if isinstance(value, dict):
            # lägg till nuvarande värden i listan och starta om funktionen från nuvarande pos
            slut_pos.append(treecoords(value, nuvarande_pos))

        # När den gått genom alla dictionaries och samlat värdena lägg till dom i listan
        else:
            slut_pos.append((nuvarande_pos, value))

    return tuple(slut_pos)  # gör om listan till tuple och returnera den


if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.

    # Exempel:

    print(treecoords({"a": 1, "b": 2}))
    print(treecoords({"x": {"y": 3}, "z": 4}))
    print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))
