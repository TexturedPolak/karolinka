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