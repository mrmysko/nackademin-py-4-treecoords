def treecoords(tree: dict, current_coord: tuple=()) -> tuple:
    '''Returns a tuple of tuples of where the values that aren't dictionaries are in a dictionary of dictionaries'''
    results=[]
    for key, value in tree.items():
        current_key = current_coord + (key, )
        if isinstance(value, dict):
            results.extend(treecoords(value, current_key))
        else:
            results.append((current_key, value))
    return tuple(results)        
            
    
    

if __name__ == "__main__":
    print(treecoords({
    "a": 1,
    "b": 2
}))
    print(treecoords({
    "x": {
        "y": 3
    },
    "z": 4
}))
    print(treecoords({
    "root": {
        "left": 5,
        "right": {
            "left": 6,
            "right": 7
        }
    }
}))
    print(treecoords({
    "1": {
        "2": {
            "3": {}
        },
        "4": {
            "5": 8,
            "6": 9
        }
    }
}))
    print(treecoords({
    "a": {
        "b": {
            "c": 10,
            "d": 11
        },
        "e": {
            "f": 12
        }
    },
    "g": 13
}))
    