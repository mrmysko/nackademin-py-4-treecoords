def treecoords(tree, config=None):
    result = []

    for key, value in tree.items():
        if isinstance(value, dict):
            sub_coords = treecoords(value)
            for coord, val in sub_coords:
                result.append(((key,) + coord, val))
        else:
            result.append(((key,), value))

    return tuple(result)


if __name__ == "__main__":
    print(treecoords({"kebab": 1, "kebabtallrik": 2}))
    print(treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}))

    print(treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}))
