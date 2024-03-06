# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.

# Skapar nästlade bibliotek och för att skapa
trad1 = {
    "name": "Tommy",
    "age": 35,
    "City": "Stockholm",
}
trad2 = {"gren1": "Ymmot", "gren2": trad1}
trad3 = {"gren3": "Nasto", "gren4": trad2}


def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # For loopen läser igenom hela trädet och söker efter
    # värderna i trädet (nyckelpar + värdet) i den angivna "tree".
    # Sedan skapas en ny variabel för koordinaterna
    # som sedan visar vägen till varje värde (ny_coord)
    # För varje iteration i loopen kollar om "value"är en
    # dictionary, då anropas funktionen rekursivt, för att
    # navigera djupare in i "trädet".

    result = []  # Skapar en tom lista
    for key, value in tree.items():  # items skriver ut keys och values
        ny_coord = current_coord + (
            key,
        )  # komman (,) i key - behövs annars kan ej python läsa den som en tuple

        # Här kollar man om value är en dictionary
        # och visar resultatet i funktionen rekursivt
        # OM value är en dictionary, då går treecords djupare
        # in i trädet rekursivt för att söka efter fler (under grenar)
        # OM inte det är en dictionary då har man nått slutet i "trädet"
        # så kallad "nästling". Vilket menas finns inget värde för att rekursivt
        # söka efter fler "grenar".
        # Som slutligen returnerar värdet i tuples
        if isinstance(value, dict):
            result.append(treecoords(value, ny_coord))
        else:
            result.append((ny_coord, value))
    return tuple(result)


if __name__ == "__main__":

    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    print(treecoords(trad1))
    print(treecoords({"a:": 1, "b:": 2}))
    print(treecoords({"c:": 3, "d:": 4, "e:": 5}))
    print(treecoords({"f:": 6, "g:": 7, "h:": 8, "i:": 9}))
    print(treecoords(trad2))
    print(treecoords(trad3))
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
