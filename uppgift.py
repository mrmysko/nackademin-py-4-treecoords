def treecoords(tree, gren=()):
    # Funktionen sätter så tree=trädet som ska undersökas,
    # gren= en tom tuple som används för att hålla reda på vilken gren vi är på.
    for key, value in tree.items():
        ny_gren = gren + (key,)
    #   Startar en loop som går igenom alla key-value par i trädet man är i just nu.
        if isinstance(value, dict):
            treecoords(value, ny_gren)
    #   Om värdet är en dictionary så går den rekursivt igenom den dictionaryn.
        else:
            print(f'key: {ny_gren}, Value: {value}')
    #   Ifall det inte är en dictionary så printar den ut nyckeln och värdet.

if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
    pass  # Ta bort denna rad
