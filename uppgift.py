def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # Skapa en tom lista för att lagra resultaten
    result = []

    # Loopa igenom varje nyckel-värde-par i trädet
    for key, value in tree.items():

        # Uppdatera den aktuella koordinaten med den nuvarande nyckeln
        new_current_coord = current_coord + (key,)
        # print("key:", (key,))
        # print("new_current_coord:", new_current_coord)

        # Om värdet är en dictionary, gör ett rekursivt anrop
        if isinstance(value, dict):

            result.extend(treecoords(value, new_current_coord))
            # print("key:", (key,))
            # print("new_current_coord:", new_current_coord)

        else:

            result.append((new_current_coord, value))

    # Konvertera listan med resultat till en tuple och returnera den
    return tuple(result)


# Exempel 1
result_1 = treecoords({"a": 1, "b": 2})
print(result_1)  # förvänta return ( (("a",), 1),(("b",), 2))

# Exempel 2
result_2 = treecoords({"x": {"y": 3}, "z": 4})
print(result_2)  # ((("x", "y"), 3),(("z",), 4))

# Exempel 3
result_3 = treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}})
print(result_3)
# # ((("root", "left"), 5),(("root", "right", "left"), 6),(("root", "right", "right"), 7))
