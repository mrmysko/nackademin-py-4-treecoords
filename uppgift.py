def treecoords(tree: dict, current_coord: tuple = ()):
    # Result tuple
    result = ()

    for key, value in tree.items():  # Iterate through key-value pairs in tree

        new_coord = current_coord + (key,)  # update coordinates

        if isinstance(value, dict):  # check if the value is a dict
            result += treecoords(value, new_coord)  # recursive call for subtree
        else:
            result += ((new_coord, value),)  # add coordinates and value to result tuple

    return result  # return result tuple


if __name__ == "__main__":
    # Exempel 1
    print(treecoords({"a": 1, "b": 2}))
    # Exempel 2
    print(treecoords({"x": {"y": 3}, "z": 4}))
    # Exempel 3
    print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))
    # Exempel 4
    print(treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}))
    # Exempel 5
    print(treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}))
