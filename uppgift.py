
def treecoords(tree: dict, current_coord: tuple=()) -> tuple:
    
    tree_value = []
    
    for key, value in tree.items():
        key_value = current_coord + (key, )
        
        if isinstance(value, dict):
            tree_value.extend(treecoords(value, key_value))
        else:
            tree_value.append(tuple((key_value, value)))
            
            
    return tuple(tree_value)
        

if __name__ == "__main__":
    
    #
    # Exempel:
    print(treecoords({
        "a": 1,
        "b": 2
    }))
    #  
    print(treecoords({
    "root": {
        "left": 5,
        "right": {
            "left": 6,
            "right": 7
            }
        }
    }))
    #
    treecoords({
    "x": {
        "y": 3
        },
        "z": 4
    })
