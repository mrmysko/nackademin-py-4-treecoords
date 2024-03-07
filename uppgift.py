# definiera en funktion som tar ett träd koordinater
def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # skapa en tom lista för resultaten
    result = []

    # iterera över varje key-value par i trädet
    for key, value in tree.items():

        # lägg till den aktuella nyckeln till de aktuella koordinaterna
        new_coord = current_coord + (key,)

        # om värdet är en dict indikerar det ett underträd
        # anropa funktionen rekursivt på underträdet och utöka resultatslistan
        if isinstance(value, dict):
            result.extend(treecoords(value, new_coord))

        # om värdet inte är en dict indikerar det en lövnod
        # lägg till koordinaterna och värdet till resultatslistan
        else:
            result.append((new_coord, value))

    # konvertera resultatslistan till en tuple och returnera den
    return tuple(result)


if __name__ == "__main__":
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
    if __name__ == "__main__":
        # Test 1
        print(treecoords({"a": 1, "b": 2}))

        # Test 2
        print(treecoords({"x": {"y": 3}, "z": 4}))

        # Test 3
        print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))

        # Test 4
        print(treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}))

        # Test 5
        print(treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}))
