# Na czym polega szyfr?

1. Wybieramy dane słowo np. słowo Karolinka, od nazwy tego szyfru.

2. Tworzymy tabelę o tylu kolumnach i tylu wierszach ile liter ma nasze słowo, w tym przypadku 9, czyli tworzymy tabele 9x9.

3. W pierwszej kolumnie, wpisujemy nasze słowo z góry na dół.

| K  | -  | -  | -  | -  | -  | -  | -  |  - |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| A  | -  |  - |  - | -  | -  | -  | -  |  - |
| R  | -  |  - |  - | -  | -  |-   | -  | -  |
| O  | -  |  - |  - | -  | -  |-   | -  | -  |
| L  | -  |  - |  - | -  | -  |-   | -  | -  |
| I  | -  |  - |  - | -  | -  |-   | -  | -  |
| N  | -  |  - |  - | -  | -  |-   | -  | -  |
| K  | -  |  - |  - | -  | -  |-   | -  | -  |
| A  | -  |  - |  - | -  | -  |-   | -  | -  |

4. Pozostałe pola w każdym wierszu uzupełniamy kolejnymi literami w alfabecie (pomijając polskie znaki)

| K  | L  | M  | N  | O  | P  | R  | S  |  T |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| A  | B  |  C |  D | E  | F  | G  | H  |  I |
| R  | S  |  T |  U | W  | Y  |Z   | A  | B  |
| O  | P  |  R |  S | T  | U  |W   | Y  | Z  |
| L  | M  |  N |  O | P  | R  |S   | T  | U  |
| I  | J  |  K |  L | M  | N  |O   | P  | R  |
| N  | O  |  P |  R | S  | T  |U   | W  | Y  |
| K  | L  |  M |  N | O  | P  |R   | S  | T  |
| A  | B  |  C |  D | E  | F  |G   | H  | I  |

5. Aby zaszyfrować dane słowo np. Python, wybieramy pozycje (współrzędne) w tabeli (kolumna x wiersz) każdej litery. 

Słowo PYTHON wygląda zaszyfrowane tak: ```2x4 6x3 9x8 8x2 7x6 4x8```

