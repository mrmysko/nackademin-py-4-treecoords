def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    result = []

    for key, value in tree.items():
        new_coord = current_coord + (key,)

        if isinstance(value, dict):
            result.extend(treecoords(value, new_coord))
        else:
            result.append((new_coord, value))

    return tuple(result)


exempel1 = {"a": 1, "b": 2}

exempel2 = {"x": {"y": 3}, "z": 4}

exempel3 = {"root": {"left": 5, "right": {"left": 6, "right": 7}}}

exempel4 = {"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}

exempel5 = {"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}

print(treecoords(exempel1))
print(treecoords(exempel2))
print(treecoords(exempel3))
print(treecoords(exempel4))
print(treecoords(exempel5))
