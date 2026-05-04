# Błędy

## Exception: Niepoprawny znak. Znak (twój znak) nie znajduje się na klawiaturze komórki

Dany znak który znajduje się w tekście do zaszyfrowania nie znajduje się na klawiaturze komórki (liczę tylko to co jest narysowane na niej), więc nie można go zaszyfrować w żaden sposób.
Rozwiązania:

1. Stwórz własną mapę w której ten znak się znajduje. Domyślna mapa to zawsze:

    ```python
     {
        ' ': '0',
        'A': '2', 
        'B': '22', 
        'C': '222', 
        'D': '3', 
        'E': '33', 
        'F': '333',
        'G': '4', 
        'H': '44',
        'I': '444', 
        'J': '5', 
        'K': '55', 
        'L': '555', 
        'M': '6', 
        'N': '66', 
        'O': '666', 
        'P': '7', 
        'Q': '77', 
        'R': '777', 
        'S': '7777', 
        'T': '8',
        'U': '88', 
        'V': '888',
        'W': '9', 
        'X': '99', 
        'Y': '999', 
        'Z': '9999'
    }
    ```

    ```python
    from karolinka import Komorkowy
    mapa = {
        ' ': '0',
        'A': '2', 
        'B': '22', 
        'C': '222', 
        'D': '3', 
        'E': '33', 
        'F': '333',
        'G': '4', 
        'H': '44',
        'I': '444', 
        'J': '5', 
        'K': '55', 
        'L': '555', 
        'M': '6', 
        'N': '66', 
        'O': '666', 
        'P': '7', 
        'Q': '77', 
        'R': '777', 
        'S': '7777', 
        'T': '8',
        'U': '88', 
        'V': '888',
        'W': '9', 
        'X': '99', 
        'Y': '999', 
        'Z': '9999'
    }
    nowy_szyfr = Komorkowy(mapa=mapa)
    ```

2. Zmień ten znak w tekście na jakiś podobny.
3. Usuń problematyczny znak z tekstu.

## Inne?

Rozwiązania:

1. Skontaktuj się z twórcą programu. Uruchom program w trybie debugowania i wyślij informacje podane w konsoli:

    ```python
    from karolinka import Komorkowy
    nowy_szyfr = Komorkowy(debug=True)
    ```
