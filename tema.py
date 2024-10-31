import pandas as pd
import os
import funkcje as f
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

class Tema:
    def __init__(self):        
        self.setting = f.setting()
        self.colEan = 'Paskowy'
        self.colCena = 'CenaZakupuNetto'
        
        #wybierz plik
        self.plik = self.sprawdzPlik(self.setting['plikTema'])
        #utwórz df
        f.naEkran(f'Pobieram dane z {self.plik}')
        self.df = pd.read_excel(self.plik, sheet_name=0)
        #sprawdz ean
        self.colEan = self.sprawdzCol(self.colEan,'EAN')
        #sprawdz cena
        self.colCena = self.sprawdzCol(self.colCena,'Cena zakupu')
        #usun wiersze bez ean
        self.df.dropna(subset=[self.colEan], inplace=True) 
        #ustaw kolumny z Tema
        self.kolumny = ['KodWlasny',self.colEan, 'NazwaZnacznika','Nazwa','IloscNaMagazynie',self.colCena]
    
    def sprawdzPlik(self,plik):
        if not os.path.isfile(plik):
            return f.szukajPlik([], 'Wskaż numer pliku w którym znajduje się kartoteka Tema: ')
        else:
            return plik

    def sprawdzCol(self,col,txt):
        if not col in self.df.columns.tolist():
            return f.szukajKol(self.df.columns.tolist(),self.plik,txt)
        else:
            return col