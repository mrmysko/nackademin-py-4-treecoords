def treecoords(tree, gren=()):
    # Funktionen sätter så tree=trädet som ska undersökas,
    # gren= en tom tuple som används för att hålla reda på vilken gren vi är på.
    resultat = ()
    if isinstance(tree, dict):
        for key, value in tree.items():
            ny_gren = gren + (key,)
    # Kollar om tree är ett dictionary, om den är det då gör den ny_gren för att sätta key till gren för att veta vart man är.
            if isinstance(value, dict):
                resultat += treecoords(value, ny_gren)
            else:
                resultat += ((ny_gren, value),)
    # Kolla om värdet man är på är dictionary, ifall den är det gör den rekursivt anrop och lägger value och ny_gren i funktionen till tupeln resultat,
    # annars om det inte är dictionary skapa tupeln resultat med rätt värden.
    else:
        resultat += ((gren, tree),)
    return resultat

träd = ({
    "root": {
        "left": 5,
        "right": {
            "left": 6,
            "right": 7
        }
    }
})

result = treecoords(träd)


for item in result:
    print(item)
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
