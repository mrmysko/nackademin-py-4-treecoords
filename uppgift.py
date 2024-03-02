# Funktion som bearbetar dictionarys och tar reda på och spottar  ut
# kordinater i form av values
def treecoords(tree: dict, current_coord: tuple = ()):
    # Skapar en tom tupel för att slutligen samla de samladen
    # värdena här
    utmatning = []
    # forloop för att gå igenom varje element i dictionary och tupel
    for key, value in tree.items():
        # --IGNORERA print("Key:", key, "Value:" value "\n")
        # uppdaterar tupeln position med kordinater i dictionary.
        # current_coord har ett tomt startvärde och det adderas en key
        # efter varje itteration i forloopen
        position = current_coord + (key,)
        # kontrollerar om value är ett dictionary
        if isinstance(value, dict):
            # om value är en dictionary så utökas utmatning med den
            # dictionary som kontrollerats
            utmatning.extend(treecoords(value, position))
        # --IGNORERA print("Key är", key, "value är", value, "current kord", current_coord, "\n")
        else:
            # om value inte är en dictionary så utökas utmatning med
            # det kontrollerade value
            utmatning.append(
                (
                    position,
                    value,
                )
            )
            # --IGNORERA print("Value", value, " vid key", key, " är inte en dictionary\n")
    return utmatning


if __name__ == "__main__":
    treecoords({"a": 1, "b": 2})
    # ((("a",), 1),("b",), 2))

    treecoords({"x": {"y": 3}, "z": 4})
    # ((("x", "y"), 3), (("z",), 4))

    treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}})
    # ((("root", "left"), 5), (("root", "right", "left"), 6), (("root", "right", "right"), 7))

    treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}})
    # ((("1", "4", "5"), 8), (("1", "4", "6"), 9))
    treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13})
# ((("a", "b", "c"), 10), (("a", "b", "d"), 11), (("a", "e", "f"), 12), (("g",), 13))
