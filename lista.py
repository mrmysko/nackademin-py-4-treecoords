def treecoords(tree: dict, current_coord: tuple = ()):
    # Result tuple
    result = ()

    for key, value in tree.items():  # Iterate through key-value pairs in tree

        new_coord = current_coord + (key,)  # update coordinates

        if isinstance(value, dict):  # check if the value is a dict
            result += treecoords(value, new_coord)  # recursive call for subtree
        else:
            result += ((new_coord, value),)  # add coordinates and value to result tuple

    return (result,)  # return result tuple


x = treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}})

print(x)


# x = treecoords(my_dict)
# print(x)

# def okande_lista(listan):
#
#    for i in list(listan):
#        print(i)
#
#    print(len(listan))
#
#
# listan = ["alfa", "beta", "hejsan", "xi", "bra"]
#
# okande_lista(listan)
#


# def okande_lista(listan):
#
#    index = 0
#    while index < len(listan):
#        listan[index] = listan[index].upper()
#        print(listan[index])
#        index += 1
#
#
# listan = ["alfa", "beta", "hejsan", "xi", "bra"]
#
# okande_lista(listan)
