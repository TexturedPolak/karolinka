import warnings

class Cezar:
    """
    Szyfr Cezara - https://karolinka.readthedocs.io/pl/0.5.0
    """

    def __init__(self, przesuniecie: int, alfabet: str = "ABCDEFGHIJKLMNOPRSTUWYZ", debug: bool = False):
        self.przesuniecie = przesuniecie
        self.alfabet = alfabet.upper()

        # Optymalizacja przesunięć
        if przesuniecie > 0:
            kierunek = 1
        elif przesuniecie < 0:
            kierunek = -1
        else:
            kierunek = 0
        self.przesuniecie = (abs(przesuniecie) % len(alfabet))
        self.kierunek = kierunek
        

    def _przesun_znak(self, znak: str, na_odwrot: bool = False) -> str:
        if znak in [" ", "\n", "\t"]:
            return znak

        if na_odwrot:
            kierunek = self.kierunek * -1
        else:
            kierunek = self.kierunek
        numer_znaku = self.alfabet.find(znak)
        
        if numer_znaku < 0:
            warnings.warn(f"Znak {repr(znak)} nie znajduje się w alfabecie. Zostanie on przepisany.")
            return znak
        
        for i in range(self.przesuniecie):
            if numer_znaku+kierunek == -1 and kierunek == -1:
                numer_znaku = len(self.alfabet)-1
            elif numer_znaku+kierunek == len(self.alfabet) and kierunek == 1:
                numer_znaku = 0
            else:
                numer_znaku += kierunek

    
        return self.alfabet[numer_znaku]

    def zaszyfruj(self, tekst_do_zaszyfrowania: str) -> str:
        """
        Szyfruje tekst_do_zaszyfrowania zgodnie z założeniami.
        Zwraca zaszyfrowany tekst zgodnie z założeniami.

        Wejście:
        (przesuniecie = 4,
        alfabet domyślny),
        "HARCERZ I HARCERKA"


        Wyjście:
        "LEWGIWD M LEWGIWOE"
        """

        tekst_do_zaszyfrowania = tekst_do_zaszyfrowania.upper()
        zaszyfrowany_tekst = ""

        for znak in tekst_do_zaszyfrowania:
            zaszyfrowany_tekst += self._przesun_znak(znak) 

        return zaszyfrowany_tekst

    def odszyfruj(self, tekst_do_odszyfrowania: str) -> str:
        """
        Odszyfrowuje tekst_do_odszyfrowania zgodnie z założeniami.
        Zwraca zaszyfrowany tekst zgodnie z założeniami.

        Wejście:
        (przesuniecie = 4,
        alfabet domyślny),
        "LEWGIWD M LEWGIWOE"


        Wyjście:
        "HARCERZ I HARCERKA"
        """

        tekst_do_odszyfrowania = tekst_do_odszyfrowania.upper()
        odszyfrowany_tekst = ""

        for znak in tekst_do_odszyfrowania:
            odszyfrowany_tekst += self._przesun_znak(znak, na_odwrot=True)

        return odszyfrowany_tekst
