def tree_height(tree: dict, node: str) -> int:
    # Basfall: Om noden är en lövnod, returnera höjden som 0
    if not tree.get(node):  # Fyll i villkoret för att avgöra om noden är en lövnod
        return 0

    # Beräkna höjden för varje barnnod rekursivt och spara resultaten i en lista
    children_heights = []
    for child_node in tree[
        node
    ]:  # Fyll i hur du får tag på barnnoderna för den aktuella noden
        child_height = tree_height(
            tree, child_node
        )  # Anropa rekursivt tree_height för att beräkna höjden för barnnoden
        children_heights.append(child_height)

    # Välj den högsta höjden bland barnen och lägg till 1 för den aktuella noden
    max_child_height = max(children_heights)
    return max_child_height + 1


# Testa din funktion
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

start_node = "A"
print(
    tree_height(tree, start_node)
)  # Förväntad utgång: Högden på trädet från startnoden
