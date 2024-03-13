# Skriptet skapar funktionen "treecoords" som tar två argument. Det första argumentet är "tree: dict" som förväntas vara en dictionry, det andra argumentet är "currect_coord: tuple" som representerar den aktuella koordinaten i trädet. Funktionen bör returnera en tuple med koordinaterna och värdena för varje element som inte är en dictionary.
# Det skapas en tom lista "coordinates = []" för att samla in koordinaterna och värdena.
# Iterering genom trädkoordinaterna med nyckel-värde-par i "tree.items()" för dictionaries. "Key" kommer innehålla nyckeln och "value" värdet för varje par.
# Skriv ut nyckeln för varje element i trädet. På så sätt kan man felsöka och se hur iterationen går igenom trädet.
# Om det aktuella värdet är en dictonary görs ett rekursivt anrop till funktionen "treecords" med det aktuella värdet som "tree", sedan uppdaterar "current_coorD" genom att lägga till den aktuella nyckeln i slutet av tupeln. Resultatet av det rekursiva anropet läggs till i "coordinates" listan med "extend()"-metoden.
# Om det aktuella värdet inte är en dictionary läggs det till en tuple som består av den aktuella koordinaten och värdet till "coordinates"-listan.
# Returnera listan med koordinaterna och värdena för alla element i trädet.


def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    coordinates = []

    for key, value in tree.items():
        print(f"Key: {key}, Value: {value}")
        if isinstance(value, dict):
            sub_coordinates = treecoords(value, current_coord + (key,))
            coordinates.extend(sub_coordinates)
        else:
            coordinates.append((current_coord + (key,), value))

    return coordinates


# Test med frukter och deras godhet på skala 0-10 samt deras namn på latin.
tree = {
    "Äpple": {"Godhet": 7, "Latin": "Malus domestica"},
    "Banan": {"Godhet": 9, "Latin": "Musa"},
    "Apelsin": {"Godhet": 6, "Latin": "Aurantiacus"},
    "Kiwi": {"Godhet": 7, "Latin": "Actinidia deliciosa"},
    "Mango": {"Godhet": 10, "Latin": "Mangifera indica"},
}

# Resultatet från funktionen "treecords" tilldelas variabel "result" med "tree" som argument.
# Printa sedan resultatet som förväntas vara en tuple med koordinaterna och värderna i varje element i "tree".
result = treecoords(tree)
print(result)
