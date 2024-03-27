def treecoords(tree: dict, current_coord=()) -> tuple:
    result = []
    for key, value in tree.items():
        new_coord = current_coord + (key,)
        if isinstance(value, dict):
            result.extend(treecoords(value, new_coord))
        else:
            result.append((new_coord, value))
    return tuple(result)


if __name__ == "__main__":
    # Testkod för funktionen
    tree1 = {"a": 1, "b": 2}
    tree2 = {"x": {"y": 3}, "z": 4}
    tree3 = {"root": {"left": 5, "right": {"left": 6, "right": 7}}}
    tree4 = {"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}
    tree5 = {"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}

    print(treecoords(tree1))
    print(treecoords(tree2))
    print(treecoords(tree3))
    print(treecoords(tree4))
    print(treecoords(tree5))
