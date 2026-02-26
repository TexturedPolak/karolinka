# Karolinkowy szyfrator czyli automatyzacja harcerskiego szyfru

(i nie, nie jestem harcerzem)

## Instalacja:

```bash
python -m pip install karolinka
```

## Użycie:

```python
from karolinka import Karolinka

nowy_szyfr = Karolinka("KAROLINKA")
zaszyfrowana_wiad = nowy_szyfr.zaszyfruj("HARCERZ I HARCERKA")
odszyfrowana_wiad = nowy_szyfr.odszyfruj("8x2 1x9 7x8 3x9 5x9 7x1 7x3\t9x9\t8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2")
```

Więcej w [dokumentacji](https://github.com/TexturedPolak/karolinka/blob/70a02a8dcad62623ca28c98927e87d951ab5e795/docs.md)