import random
alfabet = "ABCDEFGHIJKLMNOPRSTUWYZ"

"""
Tworzy dwuwymiarową tablice zgodnie z założeniami tabeli opisanymi w krokach 1, 2, 3 i 4
Potrzebna na potrzeby późniejszych operacji takich jak szyfrowanie czy odszyfrowanie 
Zwraca tą tablice (w formie znaków w listach w liście).
Przykład:
Wejście: 
"KAROLINKA"
Wyjście:
[ 
    ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 
    ['R', 'S', 'T', 'U', 'W', 'Y', 'Z', 'A', 'B'], 
    ['O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z'], 
    ['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U'], 
    ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R'], 
    ['N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y'], 
    ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'], 
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
]
"""
def utworz_tabele(słowo_klucz: str):
    # Etap 1 i 2
    tabela = [["" for y in range(len(słowo_klucz))] for x in range(len(słowo_klucz))]

    # Etap 3
    for numer_wiersza in range(len(słowo_klucz)):
        tabela[numer_wiersza][0]=słowo_klucz[numer_wiersza]

    # Etap 4
    for numer_wiersza in range(len(słowo_klucz)):
        pozycja_w_alfabecie = alfabet.find(słowo_klucz[numer_wiersza][0])

        for numer_kolumny in range(len(tabela[numer_wiersza])):
            tabela[numer_wiersza][numer_kolumny] = alfabet[pozycja_w_alfabecie]
            pozycja_w_alfabecie += 1

            # Zabezpieczenie przed przepełnieniem
            if pozycja_w_alfabecie > (len(alfabet)-1):
                pozycja_w_alfabecie = 0
        
    return tabela


"""
Przeszukuje tablice dwuwymiarową, 
wygenerowaną wcześniej przez funkcję utworz_tabele w poszukiwaniu pozycji w tej tabeli.
Zwraca rzeczywiste (czyli zaczynac liczyć od 1) pozycje tabel w formie listy krotek. 
Pierwszy element krotki oznacza kolumnę, drugi wiersz.
Przykład:
Wejście:
"H",
[ 
    ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 
    ['R', 'S', 'T', 'U', 'W', 'Y', 'Z', 'A', 'B'], 
    ['O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z'], 
    ['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U'], 
    ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R'], 
    ['N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y'], 
    ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'], 
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
]
Wyjście:
[
    (8, 2),
    (8, 9)
]
"""
def znajdz_wszystkie_pozycje(litera: str, tabela: list):
    pozycje_w_tabeli = []
    for numer_wiersza in range(len(tabela)):
        for numer_kolumny in range(len(tabela[numer_wiersza])):
            if tabela[numer_wiersza][numer_kolumny] == litera:
                pozycje_w_tabeli.append((numer_kolumny+1, numer_wiersza+1))
    return pozycje_w_tabeli


"""
Szyfruje tekst_do_zaszyfrowania zgodnie z założeniami.
Wymaga podania w argumencie tabela obiektu wygenerowanego przez funkcję utworz_tabele.
Zwraca zaszyfrowany tekst zgodnie z założeniami.
Wejście:
"HARCERZ I HARCERKA",
[ 
    ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 
    ['R', 'S', 'T', 'U', 'W', 'Y', 'Z', 'A', 'B'], 
    ['O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z'], 
    ['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U'], 
    ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R'], 
    ['N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y'], 
    ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T'], 
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
]
Wyjście:
"8x2 1x9 7x8 3x9 5x9 7x1 7x3     9x9     8x2 8x3 7x1 3x9 5x9 1x3 1x1 1x2"
"""
def szyfrowanie(tekst_do_zaszyfrowania: str, tabela: list):
    zaszyfrowany_tekst = ""
    słowa = tekst_do_zaszyfrowania.split()
    numer_słowa = 0
    for słowo in słowa:
        numer_znaku=0
        for znak in słowo:
            wszystkie_pozycje = znajdz_wszystkie_pozycje(znak, tabela)
            kolumna, wiersz = random.choice(wszystkie_pozycje)
            zaszyfrowany_tekst+=f"{kolumna}x{wiersz}"
            # Dodawanie spacji pomiędzy znakami (oprócz ostatniego)
            if numer_znaku != (len(słowo)-1):
                zaszyfrowany_tekst+=" "
            numer_znaku += 1
        # Dodawanie tabulatora pomiędzy słowami (oprócz ostatniego)
        if numer_znaku != (len(słowo)-1):
                zaszyfrowany_tekst+="\t"
        numer_słowa += 1
    print(zaszyfrowany_tekst)


print(utworz_tabele("KAROLINKA"))
szyfrowanie("HARCERZ I HARCERKA", tabela=utworz_tabele("KAROLINKA"))