def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # Skapa en tom lista för att lagra resultaten
    result = []

    # Loopa igenom varje nyckel-värde-par i trädet
    for key, value in tree.items():

        # Uppdatera den aktuella koordinaten med den nuvarande nyckeln
        current_coord = current_coord + (key,)

        # Om värdet är en dictionary, gör ett rekursivt anrop
        if isinstance(value, dict):
            # Anropa treecoords rekursivt och lagra resultatet i variabeln c
            c = treecoords(value, current_coord)
            # Lägg till c i resultatlistan
            result.append(c)
        else:
            # Om värdet inte är en dictionary, skapa en tuple med koordinaten och värdet
            a = (key,)
            b = a, value
            b = tuple(b)
            # Lägg till b i resultatlistan
            result.append(b)

    # Konvertera listan med resultat till en tuple och returnera den
    return tuple(result)


# Exempel 1
result_1 = treecoords({"a": 1, "b": 2})
print(result_1)

# Exempel 2
result_2 = treecoords({"x": {"y": 3}, "z": 4})
print(result_2)

# Exempel 3
result_3 = treecoords({"root": {"left": 5, "right": {"left": 6, "right": 7}}})
print(result_3)
