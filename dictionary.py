print(isinstance(12, int))
print(isinstance(12.0, int))
print(isinstance(12.0, float))
print(isinstance({"x": 1}, dict))
print(isinstance(["x"], list))

#           .
#    gren1 / \ gren2
#            /\
#   ugren1  /  \ ugren2

gren2_varde = {"ugren1": 10, "ugren2": "hej"}
trad = {"gren1": "", "gren2": gren2_varde}


def berakna_djup(trad, djup=0):
    pass
