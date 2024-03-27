def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    result = ()  # Skapar en tom tuple för att spara resultaten.

    for key, value in tree.items():  # Loopar igenom varje nyckelpar i tree

        if isinstance(
            value, dict
        ):  # Kontrollera om Value är en dictionary med hjälp av funktionen isinstance.

            new_coord = current_coord + (
                key,
            )  # om påståendet är sant, så sparas nuvarande kordinaters nyckel i variablen new_coord

            result += treecoords(
                value, new_coord
            )  # Använder recusion och tillkallar treecoords med variablarna 'value' och 'new_coord'.

        else:

            result += (
                (current_coord + (key,), value),
            )  # Om värdet till nyckeln inte är en dict, så sparas nuvarande kordinaterna, nyckeln och värdet till result.

    return result  # Returnerar värdet av tupeln


if __name__ == "__main__":
    # Tillkallar funktionen med
    treecoords({"a": 1, "b": 2})
    treecoords({"x": {"y": 3}, "z": 4})
    treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}})
    treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}})
    treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13})
