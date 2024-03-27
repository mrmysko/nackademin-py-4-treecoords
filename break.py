namnlista = ["bo", "john", "eva", "[STOP]", "jonathan", "bosse"]

for element in namnlista:
    if len(element) < 4:
        continue
    elif element == "[STOP]":
        break
    print(element)
