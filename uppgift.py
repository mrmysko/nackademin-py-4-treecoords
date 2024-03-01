# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.


def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # Recursion...complicated af

    # Create an empty list to store tuples.
    mod_list = []

    # Iterate over the dict.
    for key, value in tree.items():
        # Check if the value is a nested dict.
        if isinstance(value, dict):
            # Recursion - Call on itself with the nested dict as argument, and key as cordinate.
            test = treecoords(value, key)
            print(type(test))
            print(f"Recursed: {test}")
        # If not, this is the end of the "chain", add the cordinates and value to the list.
        else:
            mod_list.append((key, value))

    return mod_list

    # OK, what is the base case?...we want to return a tuple with current_coords and the value
    # {'a': 1} - lowest case. This should return as ('a',), 1)
    # return ((key,), value)


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
    print(treecoords({"a": 1}))
    print(treecoords({"a": 1, "b": 2}))
    print(treecoords({"x": {"y": 3}, "z": 4}))
    print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))
