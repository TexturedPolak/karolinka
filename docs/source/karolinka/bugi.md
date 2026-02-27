# Błędy

## Exception: Błąd szyfrowanej wiadomości. Znak (twój znak) nie znajduje się w podanym alfabecie. Usuń/zmień ten znak lub dodaj go do alfabetu.

Dany znak który znajduje się w tekście do zaszyfrowania nie znajduje się w alfabecie, więc nie można go zaszyfrować w żaden sposób.
Wyjątkami są dwa znaki: 

- spacji (program wykrywa ten znak jako rozdzielenie słów) 
- i znak nowej linii, enter, \n (jest zamieniany na znak spacji)

Rozwiązania:
1. Dodaj dany znak do alfabetu, podając swój alfabet jako opcjonalny argument klasy `Karolinka`:
```python
from karolinka import Karolinka
nowy_szyfr = Karolinka("KAROLINKA", alfabet="ABCDEFGHIJKLMNOPRSTUWYZ")
```
2. Zmień ten znak w tekście na jakiś podobny.
3. Usuń problematyczny znak z tekstu.

## Exception: Błąd zaszyfrowanej wiadomości. Zaszyfrowana wiadomość na 120% nie jest zaszyfrowana tym słowem klucz.

Próbujesz odszyfrować daną wiadomość, ale słowo klucz którego użyłeś na pewno nie służyło do zaszyfrowania tej wiadomości.

Rozwiązania:
1. Od osoby od której otrzymałeś zaszyfrowaną wiadomość zdobądź poprawne słowo klucz.
2. Być może użyto innego szyfru... i nic na to nie poradzę.

## Exception: Test tabeli się nie powiódł! Słowo klucz którego użyłeś nie wypełnia całego alfabetu. Użyj dłuższego słowa klucz lub innego alfabetu.

Oznacza to co pisze - ale tłumaczac bardziej - oznacza to, że w tabeli która zastała utworzona na podstawie słowa klucz nie znajdują się wszystkie litery alfabetu, przez co zaszyfrowanie danej informacji w której jest litera, która jest w alfabecie, ale nie jest w tabeli skończy się błędem.

Rozwiązania: 
1. Dłuższe słowo klucz - najlepiej jakby było to normalne słowo, a nie ciąg przypadkowych liter.
2. Jeśli potrzebujesz tylko paru liter - możesz podać własny alfabet jako opcjonalny argument klasy Karolinka:
```python
from karolinka import Karolinka
nowy_szyfr = Karolinka("KAROLINKA", alfabet="ABCDEFGHIJKLMNOPRSTUWYZ")
```

## Exception: (wstaw nazwę testu) się nie powiódł! Program nie działa prawidłowo! Zabraniam użycia do momentu naprawy!

Oznacza to, że z jakiegoś powodu program przestał poprawnie działać, a jego wewnętrzny test się nie powiódł.

Rozwiązania: 
1. Skontaktuj się z twórcą programu. Uruchom program w trybie debugowania i wyślij informacje podane w konsoli:
```python
from karolinka import Karolinka
słowo_klucz=? # (twoje słowo klucz)
nowy_szyfr = Karolinka(słowo_klucz, debug=True)
```

## Inne?

Rozwiązania: 
1. Skontaktuj się z twórcą programu. Uruchom program w trybie debugowania i wyślij informacje podane w konsoli:
```python
from karolinka import Karolinka
słowo_klucz=? # (twoje słowo klucz)
nowy_szyfr = Karolinka(słowo_klucz, debug=True)
```