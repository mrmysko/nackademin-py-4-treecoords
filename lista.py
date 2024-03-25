def treecoords(tree: dict, current_coord: tuple = ()):
    # resultvalue = ()
    result = ()
    for key, value in tree.items():

        new_coord = current_coord + tuple(key)
        result += ((new_coord, value),)
    # resultvalue = tuple(resultvalue) + tuple(value)
    # print(new_coord, result)
    # print("key:", key, "value:", value)
    return (result,)  # resultvalue
    # return ((("a",), "1"), (("b",), "2"))
    # else:
    #   print("Detta är inte ett dictionary")


my_dict = {"a": 1, "b": 2, "c": 3}

x = treecoords(my_dict)
print("result:", x)
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
