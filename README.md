# Karolinkowy szyfrator czyli automatyzacja harcerskiego szyfru

(i nie, nie jestem harcerzem)

## Instalacja

```bash
python -m pip install karolinka
```

## Użycie

```python
from karolinka import Karolinka

nowy_szyfr = Karolinka("KAROLINKA")
zaszyfrowana_wiad = nowy_szyfr.zaszyfruj("HARCERZ I HARCERKA")
odszyfrowana_wiad = nowy_szyfr.odszyfruj("8x2 1x9 7x8 3x9 5x9 7x1 7x3\t9x9\t8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2")
```

Więcej w [dokumentacji](https://karolinka.readthedocs.io/pl/)

## Nie jesteś programistą? Chcesz tylko tego łatwo użyć?

Gotowe rozwiązanie: https://github.com/TexturedPolak/karolinka-frontend

lub: https://texturedpolak.github.io/karolinka-frontend/
