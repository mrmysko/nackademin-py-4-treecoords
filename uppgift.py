# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.


# Treecoords
# Recursively navigates through a datastructure consisting of dictionaries
# Needs to gather in and return coordinates for every element that is not a dictionary.
# What do we need to make this stuff work?!
# * [X] FIGURE OUT HOW TO DESCRIBE WHAT'S NEEDED
# * * I don't even know how to describe what I've made.
# * [X] FIGURE OUT WHAT current_coord is for!
# * * Used for: Stuff from last recursive loop.
def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    # List used to gather all this stuff
    cats = []
    # Debug stuff again.
    # print(f"current_coord: {current_coord}\n")
    # Loop through this gigantic mess
    for key, value in tree.items():
        # Is it a dictionary inside this tree?
        if isinstance(value, dict):
            # print(f"Key: {key}, Value: {value}\n")
            # If the length of current_coord is longer than zero, this indicates that this function has been ran recursively.
            if len(current_coord) > 0:
                # Supposedly turns it into a list
                stuff = list(current_coord)
                # Contains...something?
                losing_much_pantience = []
                # Loops through the list version of current_coord
                for patience_remaining in stuff:
                    # Checks to ensure we don't add a tuple to the list, if we encounter one then we will add the stuff inside it to the list
                    if type(patience_remaining) == tuple:
                        for idontcare in patience_remaining:
                            losing_much_pantience.append(idontcare)
                    else:
                        losing_much_pantience.append(patience_remaining)
                # Adds the current key for this entry in the dictionary to that list
                losing_much_pantience.append(key)
                # Debug stuff, uncomment to see outputs.
                # print(f"losing_much_patience: {losing_much_pantience}")
                car = losing_much_pantience
            else:
                # Basically makes it a tuple, I don't remember if this else situation ever gets used.
                car = (key,)
            # Run the stuff recursively again because there's a dictionary inside a dictionary
            cater = treecoords(value, car)
            # Run through the returned values and appends the individual entries it to the cats list.
            # This is to prevent stupidity in the form of: ((("x", "y"), 3),)
            for elements in cater:
                cats.append(elements)
            # for elemental in cats:
            #    print(f"Elemental: {elemental}")
            # Loop through the inner dictionary
        else:
            # Debug print outs.
            # print(f"Key: {key}, Value: {value}\n")
            # print(f"Current current_coord: {current_coord}")
            # See the comments in the isinstance version of stuff.
            if len(current_coord) > 0:
                cateras = list(current_coord)
                losing_patience = []
                for weh in cateras:
                    if type(weh) == tuple:
                        for idk in weh:
                            losing_patience.append(idk)
                    else:
                        losing_patience.append(weh)
                losing_patience.append(key)
                # Debug print out
                # print(losing_patience)
                # Make the list into a tuple.
                a = tuple(losing_patience)
            else:
                a = (key,)
            b = a, value
            # Don't even ask, I've long since given up on trying to understand the machine spirits, it just works.
            b = tuple(b)
            # Debug stuff again
            # print(f"B is currently: {b}")
            cats.append(b)
            # Debug stuff again
            # print(f"Cats is currently: {cats}")
    trees = tuple(cats)
    # Debug stuff again
    # print(f"Trees is currently: {trees}")
    return trees


# if __name__ == "__main__":
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
#    pass  # Ta bort denna rad

# Should Return:
# (
#    (("a",), 1),
#    (("b",), 2)
# )
# print(treecoords({"a": 1, "b": 2}))

# Should Return:
# (
#    (("x", "y"), 3),
#    (("z",), 4)
# )
# print(treecoords({"x": {"y": 3}, "z": 4}))

# Should Return:
# (
#    (("root", "left"), 5),
#    (("root", "right", "left"), 6),
#    (("root", "right", "right"), 7)
# )
# print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))
