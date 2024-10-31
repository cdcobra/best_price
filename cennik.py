import os
import pandas as pd
import funkcje as f

class Cennik:
    def __init__(self, plik):
        #ustawienia
        self.setting = f.setting()
        self.plik = plik
        #ładuje plik
        self.df = pd.read_excel(plik, sheet_name=0)
        #szukam kolumn
        self.colEan = [x for x in self.setting['kolumnyEan'] if x in self.df]
        #jeżeli nie znaleziono kolumny dla EAN
        if not self.colEan:            
            self.colEan = [f.szukajKol(self.df.columns.tolist(),plik,'EAN')]
        
        self.colEan=self.colEan[0]
        self.colCena = f.szukajKol(self.df.columns.tolist(),plik,'CENA')
        #jeżeli znaleziono
        if self.colEan and self.colCena:
            f.naEkran(f'Plik: {plik} Kolumna cena: {self.colCena}, Kolumna EAN: {self.colEan}')