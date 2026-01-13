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

# Założenia automatyzatora:

1. Zaszyfrowane litery są oddzielone od siebie znakiem spacji

2. Zaszyfrowane słowa są oddzielone od siebie znakiem tabulacji lub inaczej TAB

3. W przypadku wielu pozycji danej litery w tabeli, automatyzator pseudolosuje jedną z możliwych pozycji.

# Dokumentacja

## class Szyfr

```python
nowy_szyfr = Szyfr("KAROLINKA")
```

Tworzy nowy obiekt, przechowujący tabelę potrzebną do szyfrowania i odszyfrowywania.

### func szyfruj(tekst_do_zaszyfrowania)

```python
nowy_szyfr = Szyfr("KAROLINKA")
nowy_szyfr.szyfruj("HARCERZ I HARCERKA")
```

Szyfruje tekst_do_zaszyfrowania zgodnie z [założeniami](README.md).
Zwraca zaszyfrowany tekst zgodnie z [założeniami](README.md).

Wejście:

"KAROLINKA",

"HARCERZ I HARCERKA"

Wyjście:

"8x2 1x9 7x8 3x9 5x9 7x1 7x3\t9x9\t8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2"

### func odszyfruj(tekst_do_odszyfrowania)

```python
nowy_szyfr = Szyfr("KAROLINKA")
nowy_szyfr.odszyfruj("8x2 1x9 7x8 3x9 5x9 7x1 7x3\t9x9\t8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2")
```

Odszyfrowuje tekst_do_odszyfrowania zgodnie z [założeniami](README.md).
Zwraca odszyfrowany tekst zgodnie z [założeniami](README.md).

Wejście:

"KAROLINKA",

"8x2 1x9 7x8 3x9 5x9 7x1 7x3\t9x9\t8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2"

Wyjście:

"HARCERZ I HARCERKA"

## Błędy:

### Exception: Test tekstu do zaszyfrowania się nie powiódł! Znak (twój znak) nie znajduje się w podanym alfabecie. Usuń/zmień ten znak lub dodaj go do alfabetu.

Dany znak który znajduje się w tekście do zaszyfrowania nie znajduje się w alfabecie, więc nie można go zaszyfrować w żaden sposób.
Wyjątkami są dwa znaki: 

- spacji (program wykrywa ten znak jako rozdzielenie słów) 
- i znak nowej linii, enter, \n (jest zamieniany na znak spacji)

Rozwiązania:
1. Dodaj dany znak do alfabetu, podając swój alfabet jako opcjonalny argument klasy Szyfr:
```python
nowy_szyfr = Szyfr("KAROLINKA", alfabet="ABCDEFGHIJKLMNOPRSTUWYZ")
```
2. Zmień ten znak w tekście na jakiś podobny.
3. Usuń problematyczny znak z tekstu.

### Exception: Test tabeli się nie powiódł! Słowo klucz którego użyłeś nie wypełnia całego alfabetu. Użyj dłuższego słowa klucz lub innego alfabetu.


Oznacza to co pisze - ale tłumaczac bardziej - oznacza to, że w tabeli która zastała utworzona na podstawie słowa klucz nie znajdują się wszystkie litery alfabetu, przez co zaszyfrowanie danej informacji w której jest litera, która jest w alfabecie, ale nie jest w tabeli skończy się błędem.

Rozwiązania: 
1. Dłuższe słowo klucz - najlepiej jakby było to normalne słowo, a nie ciąg przypadkowych liter.
2. Jeśli potrzebujesz tylko paru liter - możesz podać własny alfabet jako opcjonalny argument klasy Szyfr:
```python
nowy_szyfr = Szyfr("KAROLINKA", alfabet="ABCDEFGHIJKLMNOPRSTUWYZ")
```

### Exception: (wstaw nazwę testu) się nie powiódł! Program nie działa prawidłowo! Zabraniam użycia do momentu naprawy!

Oznacza to, że z jakiegoś powodu program przestał poprawnie działać, a jego wewnętrzny test się nie powiódł.

Rozwiązania: 
1. Skontaktuj się z twórcą programu. Uruchom program w trybie debugowania i wyślij informacje podane w konsoli:
```python
słowo_klucz=? # (twoje słowo klucz)
nowy_szyfr = Szyfr(słowo_klucz, debug=True)
```

### Inne?

Rozwiązania: 
1. Skontaktuj się z twórcą programu. Uruchom program w trybie debugowania i wyślij informacje podane w konsoli:
```python
słowo_klucz=? # (twoje słowo klucz)
nowy_szyfr = Szyfr(słowo_klucz, debug=True)
```
