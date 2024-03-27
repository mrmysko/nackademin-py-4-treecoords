
coords = []

def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    """Return a tuple of tuples that describes tree paths from root to leaf.

    Arguments:
        tree (dict): A dictionary describing a tree with one or multiple roots.
        current_cord (tuple): The aggregated tree path from a specific root.

    Returns:
        tuple
    """

    global coords
    reset = True if not current_coord else False
    coords = [] if reset else coords

    for name, node in tree.items():
        leaf = True if not isinstance(node, dict) or node == {} else False
        coord = current_coord + (name,)
        if leaf:
            if node:
                coords.append((coord, node))
        else:
            treecoords(node, coord)
    return tuple(coords)
        


if __name__ == "__main__":
    print(treecoords({"a": 1,"b": 2}))
    print(treecoords({"x": {"y": 3}, "z": 4}))
    print(treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}}))
    print(treecoords({"1": {"2": {"3": {}}, "4": {"5": 8, "6": 9}}}))
    print(treecoords({"a": {"b": {"c": 10, "d": 11}, "e": {"f": 12}}, "g": 13}))
