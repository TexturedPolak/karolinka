# Założenia automatyzatora

1. Zaszyfrowane litery są oddzielone od siebie znakiem spacji

2. Zaszyfrowane słowa są oddzielone od siebie znakiem końca linii (znak `\n` lub potocznie ENTER)

3. W przypadku wielu pozycji danej litery w tabeli, automatyzator pseudolosuje jedną z możliwych pozycji.

4. Jeżeli znaku nie ma w alfabecie, zostanie przepisany w formie niezaszyfrowanej. Wyjątkiem są znaki `\n` (ENTER), `\t` (TAB) i znak spacji - są już wykorzystywane przez program do składni.
