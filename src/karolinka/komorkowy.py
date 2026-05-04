import warnings

class Komorkowy:
    """
    Szyfr Komórkowy - https://karolinka.readthedocs.io/pl/0.6.0
    """

    def __init__(self, mapa: dict = None, debug: bool = False):
        if mapa is None:
            self.mapa = self.wygeneruj_mape()
        else:
            self.mapa = mapa

    def wygeneruj_mape(self) -> dict:
        """
        Generuje domyślną mapę znaków.
        
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
        """
        liczba_klikniec = 1
        numer = 2
        mapa = {" ": str(0)}
        for znak in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mapa[znak] = str(numer) * liczba_klikniec
            if liczba_klikniec == 3 and numer in [1, 2, 3, 4, 5, 6, 8]:
                liczba_klikniec = 0
                numer += 1 
            elif liczba_klikniec == 4 and numer in [7, 9]:
                liczba_klikniec = 0
                numer += 1 
            liczba_klikniec += 1
        return mapa
    
    def zaszyfruj(self, tekst_do_zaszyfrowania: str) -> int:
        """
        Szyfruje tekst_do_zaszyfrowania zgodnie z założeniami.
        Zwraca zaszyfrowany tekst zgodnie z założeniami.

        Wejście:
        (domyślna mapa),
        "HARCERZ I HARCERKA"

        Wyjście:
        4427772223377799990444044277722233777552
        """
        tekst_do_zaszyfrowania = tekst_do_zaszyfrowania.upper()
        zaszyfrowany_tekst = ""

        for znak in tekst_do_zaszyfrowania:
            zaszyfrowany_znak = self.mapa.get(znak)
            if zaszyfrowany_znak is None:
                raise Exception(f"Niepoprawny znak. Znak {repr(znak)} nie znajduje się na klawiaturze komórki.")
            zaszyfrowany_tekst += zaszyfrowany_znak
        
        return int(zaszyfrowany_tekst)

    def odszyfruj(self, tekst_do_odszyfrowania: int) -> str:
        """
        Odszyfrowuje tekst_do_odszyfrowania zgodnie z założeniami.
        Zwraca zaszyfrowany tekst zgodnie z założeniami.

        Wejście:
        (domyślna mapa),
        4427772223377799990444044277722233777552

        Wyjście:
        "HARCERZ I HARCERKA"
        """
        tekst_do_odszyfrowania = str(tekst_do_odszyfrowania)

        # Oddzielenie pojedynczych znaków od siebie
        poprzednia = tekst_do_odszyfrowania[0]
        znak = ""
        znaki = []
        for cyfra in tekst_do_odszyfrowania:
            if poprzednia == cyfra:
                znak += cyfra
            else:
                znaki.append(znak)
                znak = cyfra

            poprzednia = cyfra
        znaki.append(znak)

        # Właściwe odszyfrowywanie
        odszyfrowany_tekst = ""
        for znak in znaki:
            for klucz, wartosc in self.mapa.items():
                if wartosc == znak:
                    odszyfrowany_tekst += klucz

        return odszyfrowany_tekst