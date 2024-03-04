[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/1kTndXhL)
# Uppgift 4 - Trädkoordinater

## <a name='Syfte'></a>Syfte

Att lära ut hur man rekursivt navigerar genom en datastruktur bestående av
dictionaries (dict i dict), samt hur man hanterar och returnerar data baserat på
denna navigering.

<!-- vscode-markdown-toc -->

- [Syfte](#Syfte)
- [Förberedelser](#Frberedelser)
- [Beskrivning](#Beskrivning)
  - [Detaljer](#Detaljer)
    - [Skapa en funktion](#Skapaenfunktion)
- [Tips](#Tips)
  - [Använda `items()`-metoden](#Anvndaitems-metoden)
  - [Kontrollera om ett element är en dictionary](#Kontrolleraomettelementrendictionary)
  - [Rekursionstips](#Rekursionstips)
    - [Hantera rekursiva returvärden](#Hanterarekursivareturvrden)
- [Exempel](#Exempel)
  - [Exempel 1](#Exempel1)
  - [Exempel 2](#Exempel2)
  - [Exempel 3](#Exempel3)
  - [Exempel 4](#Exempel4)
  - [Exempel 5](#Exempel5)
  - [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Frberedelser'></a>Förberedelser

- Se till att du är bekväm med grundläggande Python-syntax, särskilt
  dictionaries och tuple.
- Repetera rekursion och hur det kan användas för att lösa problem.

## <a name='Beskrivning'></a>Beskrivning

I denna uppgift ska du skriva en funktion `treecoords` som rekursivt navigerar
genom en datastruktur bestående av dictionaries. Funktionen ska samla och
returnera koordinater och värden för varje element som inte är en dictionary.

### <a name='Detaljer'></a>Detaljer

#### <a name='Skapaenfunktion'></a>Skapa en funktion

- **Funktionsignatur:** `def treecoords(tree: dict, current_coord: tuple=()) ->
tuple:`
- **Vad den ska göra:** Funktionen ska ta ett "träd" (en dictionary som kan
  innehålla andra dictionaries) och rekursivt gå igenom varje element.
- **Vad den ska returnera:** En tuple av tuples. Varje element i den inre tupeln
  ska vara en tuple med ("koordinat", värde), där "koordinat" är en tuple som
  representerar vägen (nycklarna) man måste följa för att nå värdet.

Självklart! Här lägger jag till några tips som kan hjälpa studenterna att bättre
förstå och genomföra uppgiften, särskilt med fokus på rekursion och hantering av
dictionaries.

## <a name='Tips'></a>Tips

### <a name='Anvndaitems-metoden'></a>Använda `items()`-metoden

- Varje dictionary i Python har en metod som heter `items()`. Denna metod
  returnerar en lista av tuple-par, där varje tuple innehåller en nyckel och
  dess motsvarande värde. Använd denna metod för att iterera över både nycklar
  och värden i ditt dictionary. Exempel:
  ```python
  for key, value in my_dict.items():
      print(f"Key: {key}, Value: {value}")
  ```

### <a name='Kontrolleraomettelementrendictionary'></a>Kontrollera om ett element är en dictionary

- För att avgöra om ett visst värde i ditt träd (dictionary) är en
  underdictionary, kan du använda `isinstance()`-funktionen. Detta är särskilt
  användbart för att avgöra om du ska göra ett rekursivt anrop eller inte.
  Exempel:
  ```python
  if isinstance(value, dict):
      # Gör ett rekursivt anrop
  else:
      # Hantera värdet som inte är en dictionary
  ```

### <a name='Rekursionstips'></a>Rekursionstips

- När du anropar din funktion rekursivt, kom ihåg att uppdatera dina argument på
  ett sätt som reflekterar din nuvarande position i trädet. Detta innebär ofta
  att du lägger till den nuvarande nyckeln till din "koordinat"-tuple.
- Tänk på basfallet för din rekursion. I detta fall är basfallet när funktionen
  når ett värde som inte är en dictionary. Vid detta läge ska funktionen
  returnera koordinaten och värdet istället för att göra ytterligare rekursiva
  anrop.
- Kom ihåg att samla ihop värdena från dina rekursiva anrop. Eftersom varje
  anrop returnerar en tuple av tuples, behöver du sätta ihop dessa till en enda
  tuple som du sedan returnerar från funktionen. Detta kan göras genom att
  använda tuple-konkatenering eller genom att samla ihop resultaten i en lista
  som sedan konverteras till en tuple.

#### <a name='Hanterarekursivareturvrden'></a>Hantera rekursiva returvärden

- Ett vanligt misstag vid rekursion är att inte korrekt hantera returvärden från
  rekursiva anrop. Se till att du samlar ihop och returnerar dessa värden på ett
  korrekt sätt. Om din funktion ska returnera en tuple av tuples, och varje
  rekursivt anrop returnerar en del av denna tuple, måste du se till att dessa
  delar samlas ihop korrekt.
- Ett sätt att hantera detta är att initiera en tom lista i början av din
  funktion, och sedan fylla på denna lista med resultat från varje rekursivt
  anrop (eller direkt med värden om de inte är dictionaries). När alla rekursiva
  anrop är klara, kan du konvertera denna lista till en tuple och returnera den.

Genom att följa dessa tips bör studenterna få en bättre förståelse för hur man
navigerar och manipulerar datastrukturer med rekursion, samt hur man effektivt
använder Python's inbyggda funktioner för att arbeta med dictionaries. Absolut,
här är exemplen uppdaterade med returvärdena uppdelade över flera rader för ökad
läsbarhet, speciellt när det finns fler än tre element i returdatat.

## <a name='Exempel'></a>Exempel

### <a name='Exempel1'></a>Exempel 1

**Anrop:**

```python
treecoords({
    "a": 1,
    "b": 2
})
```

**Förväntad utskrift:** Inget!  
**Förväntat returvärde:**

```python
(
    (("a",), 1),
    (("b",), 2)
)
```

### <a name='Exempel2'></a>Exempel 2

**Anrop:**

```python
treecoords({
    "x": {
        "y": 3
    },
    "z": 4
})
```

**Förväntad utskrift:** Inget!  
**Förväntat returvärde:**

```python
(
    (("x", "y"), 3),
    (("z",), 4)
)
```

### <a name='Exempel3'></a>Exempel 3

**Anrop:**

```python
treecoords({
    "root": {
        "left": 5,
        "right": {
            "left": 6,
            "right": 7
        }
    }
})
```

**Förväntad utskrift:** Inget!  
**Förväntat returvärde:**

```python
(
    (("root", "left"), 5),
    (("root", "right", "left"), 6),
    (("root", "right", "right"), 7)
)
```

### <a name='Exempel4'></a>Exempel 4

**Anrop:**

```python
treecoords({
    "1": {
        "2": {
            "3": {}
        },
        "4": {
            "5": 8,
            "6": 9
        }
    }
})
```

**Förväntad utskrift:** Inget!  
**Förväntat returvärde:**

```python
(
    (("1", "4", "5"), 8),
    (("1", "4", "6"), 9)
)
```

### <a name='Exempel5'></a>Exempel 5

**Anrop:**

```python
treecoords({
    "a": {
        "b": {
            "c": 10,
            "d": 11
        },
        "e": {
            "f": 12
        }
    },
    "g": 13
})
```

**Förväntad utskrift:** Inget!  
**Förväntat returvärde:**

```python
(
    (("a", "b", "c"), 10),
    (("a", "b", "d"), 11),
    (("a", "e", "f"), 12),
    (("g",), 13)
)
```

### <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `uppgift.py`:**

   - Din lösning på uppgiften ska skrivas i `uppgift.py`. Det finns specifika
     instruktioner i `uppgift.py` om var du ska placera din källkod.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "Request Changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du väljer Merge.
   - Vid "Request Changes" är det viktigt att noggrant granska feedbacken och
     göra de nödvändiga justeringarna baserat på utbildarens anvisningar för att
     säkerställa att din uppgift uppfyller alla krav.
   - Efter att utbildaren har gjort "Approve" på din inlämning, får du göra en
     "Merge" av din "Feedback"-pull request, men inte förrän ett godkännande har
     erhållits.

6. **Initiera diskussioner i "Feedback"-pull requesten:**

   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din "Feedback"-pull request. Detta är en viktig del
     av inlärningsprocessen, där du kan ställa frågor, begära förtydliganden
     eller diskutera lösningar och feedback med din utbildare. Att engagera sig
     i dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav
     och förbättra din kod baserat på interaktionen.

## <a name='Anteckningar'></a>Anteckningar

Inga.
