# Błędy

## UserWarning: Znak (twój znak) nie znajduje się w alfabecie. Zostanie on przepisany

Informacja, że ten znak nie został zaszyfrowany, bo nie było w alfabecie.

Rozwiązania:

1. Jeżeli chcesz aby został zaszyfrowany dodaj go do alfabetu.

2. Jeżeli nie, nie musisz nic robić. Program przepisze ten znak "jak jest". Tak zostało to zaprojektowane.

## Inne?

Rozwiązania:

1. Skontaktuj się z twórcą programu. Uruchom program w trybie debugowania i wyślij informacje podane w konsoli:

    ```python
    from karolinka import Cezar
    przesuniecie = ?
    nowy_szyfr = Karolinka(przesuniecie, debug=True)
    ```
