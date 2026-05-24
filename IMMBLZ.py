from abc import ABC
from datetime import datetime


# AUTO (ABSZTRAKT OSZTÁLY)

class Auto(ABC):

    def __init__(self, rendszam, tipus, berleti_dij):
        self.__rendszam = rendszam
        self.__tipus = tipus
        self.__berleti_dij = berleti_dij

    @property
    def rendszam(self):
        return self.__rendszam

    @property
    def tipus(self):
        return self.__tipus

    @property
    def berleti_dij(self):
        return self.__berleti_dij

    def __str__(self):
        return f"{self.__tipus} - {self.__rendszam} - {self.__berleti_dij} Ft/nap"


# SZEMÉLYAUTÓ

class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, ulohelyek):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__ulohelyek = ulohelyek

    @property
    def ulohelyek(self):
        return self.__ulohelyek


# TEHERAUTÓ

class Teherauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.__teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self.__teherbiras


# BÉRLÉS

class Berles:

    def __init__(self, auto, datum):
        self.__auto = auto
        self.__datum = datum

    @property
    def auto(self):
        return self.__auto

    @property
    def datum(self):
        return self.__datum

    def __str__(self):
        return f"{self.__auto.tipus} ({self.__auto.rendszam}) - {self.__datum}"


# AUTÓKÖLCSÖNZŐ

class Autokolcsonzo:

    def __init__(self, nev):
        self.__nev = nev
        self.__autok = []
        self.__berlesek = []

    def auto_hozzaadas(self, auto):
        self.__autok.append(auto)

    def berles_hozzaadas(self, berles):
        self.__berlesek.append(berles)

    def autok_listazasa(self):

        print("\n=== ELÉRHETŐ AUTÓK ===")

        for auto in self.__autok:
            print(auto)

    def berlesek_listazasa(self):

        print("\n=== AKTUÁLIS BÉRLÉSEK ===")

        if not self.__berlesek:
            print("Nincs aktív bérlés.")
            return

        for index, berles in enumerate(self.__berlesek, start=1):
            print(f"{index}. {berles}")

    def auto_berles(self, rendszam, datum):

        # Dátum ellenőrzés
        try:
            datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            print("Hibás dátum formátum! Használd: YYYY-MM-DD")
            return

        # Autó keresése
        auto = None

        for a in self.__autok:
            if a.rendszam == rendszam:
                auto = a
                break

        if auto is None:
            print("Nincs ilyen rendszámú autó.")
            return

        # Foglaltság ellenőrzés
        for berles in self.__berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                print("Az autó már foglalt ezen a napon.")
                return

        # Új bérlés létrehozása
        uj_berles = Berles(auto, datum)
        self.__berlesek.append(uj_berles)

        print("\nSikeres bérlés!")
        print(f"Fizetendő összeg: {auto.berleti_dij} Ft")

    def berles_lemondas(self, rendszam, datum):

        for berles in self.__berlesek:

            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.__berlesek.remove(berles)
                print("Bérlés sikeresen lemondva.")
                return

        print("Nem található ilyen bérlés.")


# PROGRAM INDÍTÁS

kolcsonzo = Autokolcsonzo("Autókölcsönző")

# Autók létrehozása
auto1 = Szemelyauto("LVZ-043", "Nissan GT-R 2010", 45000, 4)
auto2 = Szemelyauto("AE CP-175", "Mitsubishi Lancer Evo X 2009", 50000, 5)
auto3 = Teherauto("UGO-270", "GMC Vandura 1983", 65000, 1000)

# Autók hozzáadása
kolcsonzo.auto_hozzaadas(auto1)
kolcsonzo.auto_hozzaadas(auto2)
kolcsonzo.auto_hozzaadas(auto3)

# Előre feltöltött bérlések
kolcsonzo.berles_hozzaadas(Berles(auto1, "2026-05-04"))
kolcsonzo.berles_hozzaadas(Berles(auto2, "2026-05-05"))
kolcsonzo.berles_hozzaadas(Berles(auto3, "2026-05-06"))
kolcsonzo.berles_hozzaadas(Berles(auto1, "2026-05-07"))


# MENÜ

while True:

    print("\n=========================")
    print(" Revved Up Autókölcsönző ")
    print("=========================")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Bérlés lemondása")
    print("4 - Bérlések listázása")
    print("0 - Kilépés")

    valasztas = input("\nVálasztás: ")

    if valasztas == "1":

        kolcsonzo.autok_listazasa()

    elif valasztas == "2":

        rendszam = input("Add meg a rendszámot: ")
        datum = input("Add meg a dátumot (YYYY-MM-DD): ")

        kolcsonzo.auto_berles(rendszam, datum)

    elif valasztas == "3":

        rendszam = input("Add meg a rendszámot: ")
        datum = input("Add meg a dátumot (YYYY-MM-DD): ")

        kolcsonzo.berles_lemondas(rendszam, datum)

    elif valasztas == "4":

        kolcsonzo.berlesek_listazasa()

    elif valasztas == "0":

        print("Program bezárva.")
        break

    else:

        print("Érvénytelen menüpont!")