import random
from .karolinka_types import Tabela



class Karolinka:
    """
    Szyfr Karolinka
    """


    class Tabela(Tabela):
        pass


    def __init__(self, słowo_klucz: str, alfabet: str = "ABCDEFGHIJKLMNOPRSTUWYZ", debug: bool = False): 
        self.debug = debug
        # Szybki test musi być uruchomiany od razu po debug - inaczej nadpisze alfabet, słowo_klucz i tabelę
        self._szybki_test() 
        self.alfabet = alfabet
        słowo_klucz = słowo_klucz.upper()
        self.słowo_klucz = słowo_klucz
        self.tabela = self._utworz_tabele(słowo_klucz)
        self._test_tabeli()


    def _utworz_tabele(self, słowo_klucz: str) -> Tabela:
        """
        Tworzy dwuwymiarową tablice zgodnie z założeniami, potrzebną na potrzeby późniejszych operacji takich jak szyfrowanie czy odszyfrowanie.

        Zwraca tą tablice (w formie znaków w listach w liście).

        Wejście: 

        "KAROLINKA"

        Wyjście: \n
        [
            ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'], \n
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], \n
            ['R', 'S', 'T', 'U', 'W', 'Y', 'Z', 'A', 'B'], \n
            ['O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z'], \n
            ['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U'], \n
            ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R'], \n
            ['N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y'], \n
            ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'], \n
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] \n
        ]
        """
        # Etap 1 i 2
        tabela = [["" for y in range(len(słowo_klucz))] for x in range(len(słowo_klucz))]

        # Etap 3
        for numer_wiersza in range(len(słowo_klucz)):
            tabela[numer_wiersza][0] = słowo_klucz[numer_wiersza]

        # Etap 4
        for numer_wiersza in range(len(słowo_klucz)):
            pozycja_w_alfabecie = self.alfabet.find(słowo_klucz[numer_wiersza][0])

            for numer_kolumny in range(len(tabela[numer_wiersza])):
                tabela[numer_wiersza][numer_kolumny] = self.alfabet[pozycja_w_alfabecie]
                pozycja_w_alfabecie += 1

                # Zabezpieczenie przed przepełnieniem
                if pozycja_w_alfabecie > (len(self.alfabet)-1):
                    pozycja_w_alfabecie = 0
        
        tabela = self.Tabela(tabela)
        return tabela


    def _znajdz_wszystkie_pozycje(self, litera: str) -> list[tuple[int]]:
        """
        Przeszukuje tabelę w poszukiwaniu pozycji danej litery w tej tabeli.

        Zwraca rzeczywiste (czyli zaczynac liczyć od 1) pozycje tabel w formie listy krotek. 

        Pierwszy element krotki oznacza kolumnę, drugi wiersz.

        Wejście:

        "H"

        (słowo klucz "KAROLINKA", alfabet domyślny)
        
        Wyjście:

        [
            (8, 2), \n
            (8, 9) \n
        ]
        """
        tabela = self.tabela
        pozycje_w_tabeli = []
        for numer_wiersza in range(len(tabela)):
            for numer_kolumny in range(len(tabela[numer_wiersza])):
                if tabela[numer_wiersza][numer_kolumny] == litera:
                    pozycje_w_tabeli.append((numer_kolumny+1, numer_wiersza+1))
        return pozycje_w_tabeli


    def zaszyfruj(self, tekst_do_zaszyfrowania: str) -> str:
        """
        Szyfruje tekst_do_zaszyfrowania zgodnie z założeniami.
        Zwraca zaszyfrowany tekst zgodnie z założeniami.

        Wejście:

        "HARCERZ I HARCERKA"

        (słowo klucz "KAROLINKA", alfabet domyślny)

        Wyjście:

        "8x2 1x9 7x8 3x9 5x9 7x1 7x3\\n9x9\\n8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2"

        Wewnętrzna notatka: Jest zależna od funkcji znajdz_wszystkie_pozycje, która wymaga tabeli.
        """
        tekst_do_zaszyfrowania = tekst_do_zaszyfrowania.upper()
        tekst_do_zaszyfrowania = tekst_do_zaszyfrowania.replace("\n", " ")
        zaszyfrowany_tekst = ""
        słowa = tekst_do_zaszyfrowania.split()
        numer_słowa = 0
        for słowo in słowa:
            numer_znaku = 0
            for znak in słowo:
                wszystkie_pozycje = self._znajdz_wszystkie_pozycje(znak)
                if len(wszystkie_pozycje) == 0:
                    if self.debug:
                        print("Test tekstu do zaszyfrowania: Not OK!")
                        print("Słowo klucz:")
                        print(repr(self.słowo_klucz))
                        print("Tabela:")
                        [print(x) for x in self.tabela]
                        print("Tekst do zaszyfrowania:")
                        print(repr(tekst_do_zaszyfrowania))
                    raise Exception(f'Błąd szyfrowanej wiadomości. Znak "{repr(znak)}" nie znajduje się w podanym alfabecie. Usuń/zmień ten znak lub dodaj go do alfabetu.')
                kolumna, wiersz = random.choice(wszystkie_pozycje)
                zaszyfrowany_tekst += f"{kolumna}x{wiersz}"
                # Dodawanie spacji pomiędzy znakami (oprócz ostatniego)
                if numer_znaku != (len(słowo)-1):
                    zaszyfrowany_tekst += " "
                numer_znaku += 1
            # Dodawanie znaku końca linii pomiędzy słowami (oprócz ostatniego)
            if numer_słowa != (len(słowa)-1):
                    zaszyfrowany_tekst += "\n"
            numer_słowa += 1
        if self.debug:
            print("Test tekstu do zaszyfrowania: OK")
        return zaszyfrowany_tekst

    
    def odszyfruj(self, tekst_do_odszyfrowania: str) -> str:
        """
        Odszyfrowuje tekst_do_odszyfrowania zgodnie z założeniami.
        Zwraca odszyfrowany tekst zgodnie z założeniami.

        Wejście:

        "8x2 1x9 7x8 3x9 5x9 7x1 7x3\\n9x9\\n8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2" (lub \\t zamiast \\n, aby wspierać starsze wersje)

        (słowo klucz "KAROLINKA", alfabet domyślny)

        Wyjście:

        "HARCERZ I HARCERKA"

        Wewnętrzna notatka: Wymaga tabeli.
        """
        tabela = self.tabela
        odszyfrowany_tekst = ""
        tekst_do_odszyfrowania = tekst_do_odszyfrowania.replace("\t", "\n") # Kompatybilność ze starszymi wersjami
        wyrazy = tekst_do_odszyfrowania.split("\n")
        numer_wyrazu = 0
        for wyraz in wyrazy:
            litery = wyraz.split()
            for litera in litery:
                kolumna, wiersz = litera.split("x")
                kolumna = int(kolumna)
                wiersz = int(wiersz)
                if kolumna > len(self.słowo_klucz) or wiersz > len(self.słowo_klucz):
                    if self.debug:
                        print("Test tekstu do odszyfrowania: Not OK!")
                        print("Słowo klucz:")
                        print(repr(self.słowo_klucz))
                        print("Tabela:")
                        [print(x) for x in self.tabela]
                        print("Tekst do odszyfrowania:")
                        print(repr(tekst_do_odszyfrowania))
                    raise Exception("Błąd zaszyfrowanej wiadomości. Zaszyfrowana wiadomość na 120% nie jest zaszyfrowana tym słowem klucz.")
                odszyfrowany_tekst += tabela[wiersz-1][kolumna-1]
            if numer_wyrazu != (len(wyrazy)-1):
                    odszyfrowany_tekst += " "
            numer_wyrazu += 1
        if self.debug:
            print("Test tekstu do odszyfrowania: OK")
        return odszyfrowany_tekst
    
   
    def _szybki_test(self) -> bool | None:
        """
        Testuje poprawność wykonywania się kodu w danych warunkach (test syntetyczny). Nadpisuje wartości podane przez użytkownika.
        """
        self.alfabet = "ABCDEFGHIJKLMNOPRSTUWYZ"
        self.słowo_klucz = "KAROLINKA"
        self.tabela = self._utworz_tabele(self.słowo_klucz)
        if self.odszyfruj(self.zaszyfruj("HARCERZ I HARCERKA")) == "HARCERZ I HARCERKA":
            if self.debug:
                print("Szybki test: OK")
                return True
        else:
            if self.debug:
                print("Szybki test: Not OK!")
                print("Słowo klucz:")
                print(repr(self.słowo_klucz))
                print("Tabela:")
                [print(x) for x in self.tabela]
                print("Zaszyfrowany tekst HARCERZ I HARCERKA:")
                test = self.zaszyfruj("HARCERZ I HARCERKA")
                print(repr(test))
                print("Odszyfrowany tekst powyżej:")
                print(self.odszyfruj(test))
            raise Exception("Szybki test się nie powiódł! Program nie działa prawidłowo! Zabraniam użycia do momentu naprawy!")

    
    def _test_tabeli(self) -> bool | None:
        """
        Testuje czy tabela wypełnia cały alfabet.
        """
        for litera in self.alfabet:
            if len(self._znajdz_wszystkie_pozycje(litera)) == 0:
                if self.debug:
                    print("Test tabeli: Not OK!")
                    print("Słowo klucz:")
                    print(repr(self.słowo_klucz))
                    print("Tabela:")
                    [print(x) for x in self.tabela]
                raise Exception("Test tabeli się nie powiódł! Słowo klucz którego użyłeś nie wypełnia całego alfabetu. Użyj dłuższego słowa klucz lub innego alfabetu.")
        if self.debug:
            print("Test tabeli: OK")
            return True
               

if __name__ == "__main__":
    debug = True
else:
    debug = False

# TESTY
testowy_obiekt = Karolinka("karolinka", debug = debug)

# TEST 1
if testowy_obiekt.odszyfruj(testowy_obiekt.zaszyfruj("HARCERZ I HARCERKA")) == "HARCERZ I HARCERKA":
    if testowy_obiekt.debug:
        print("Test 1: OK")
else:
    if testowy_obiekt.debug:
        print("Test 1: Not OK!")
        print("Słowo klucz:")
        print(repr(testowy_obiekt.słowo_klucz))
        print("Tabela:")
        [print(x) for x in testowy_obiekt.tabela]
        print("Zaszyfrowany tekst HARCERZ I HARCERKA:")
        test = testowy_obiekt.zaszyfruj("HARCERZ I HARCERKA")
        print(repr(test))
        print("Odszyfrowany tekst powyżej:")
        print(testowy_obiekt.odszyfruj(test))
    raise Exception("Test 1 się nie powiódł! Program nie działa prawidłowo! Zabraniam użycia do momentu naprawy!")



