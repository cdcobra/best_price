import pandas as pd
import os
from tema import Tema
import funkcje as f
from cennik import Cennik

class Wynik:
    def __init__(self):
        self.setting = f.setting()
        #odczytaj plik Tema
        self.tema = Tema()
        #kolumny startowe
        self.kolumny = self.listaKolumn(self.tema.colEan, self.tema.colCena)
        #kolumny cena
        self.kolumnyCena = [self.tema.colCena]
        #przygotowanie DataFrame
        self.df = pd.DataFrame(columns=self.kolumny)
        #kopuj kolumny
        self.kopujKolumny()
        #sortuj
        self.df = self.df.sort_values(['NazwaZnacznika','Nazwa'], ignore_index=True)

        #dodaj pozostale kolumny
        for plik in os.listdir("."):
            if (plik.endswith(".xlsx") or plik.endswith(".xls")) and plik not in [self.setting['plikWyniku'], self.tema.plik]:
                self.dodajKolumne(Cennik(plik))

    def dodajKolumne(self,cennik):
        #dodaj nagłówek
        self.df[cennik.plik] = None
        #aktualizacja kolumne z cenami
        self.kolumnyCena.append(cennik.plik)
        #sprawdz wg Tema
        for index, row in self.df.iterrows():
            find = cennik.df.index[cennik.df[cennik.colEan]==row[self.tema.colEan]].tolist()
            if find:
                self.df.at[index, cennik.plik] = f.liczba(cennik.df.loc[find[0], cennik.colCena])

    def kopujKolumny(self):
        for kol in self.kolumny:
            if kol in self.tema.df:
                self.df[kol] = self.tema.df[kol]

    def listaKolumn(self,colEan, colCena):
        kolumny = self.setting['kolumnyDodatkowe']
        kolumny.append(colCena)
        kolumny.insert(0, colEan)
        return kolumny
