import xlsxwriter
import pandas as pd
import funkcje as f
from wynik import Wynik

class Excel:
    def __init__(self):
        self.setting = f.setting()
        self.wynik = Wynik()
        self.writer = pd.ExcelWriter(self.setting['plikWyniku'], engine='xlsxwriter', datetime_format='dd.mm.yyyy hh:mm:ss', date_format='dd.mm.yyyy')
        self.wynik.df.to_excel(self.writer, index=False)
        workbook  = self.writer.book
        worksheet = self.writer.sheets["Sheet1"]
        (max_row, max_col) = self.wynik.df.shape
        worksheet.set_column(0,  max_col - 1, 12)
        worksheet.autofilter(0, 0, max_row, max_col - 1)
        worksheet.autofit()
        worksheet.freeze_panes(1, 0)

        #koloruj najlepsze ceny
        cf = workbook.add_format({'bg_color': '#4FFF33'})
        for index,row in self.wynik.df.iterrows():    
            cena = min(filter(None,row[self.wynik.kolumnyCena].tolist()), default=0)
            for _kol in self.wynik.kolumnyCena:
                if(cena==row[_kol]):
                    colIdx = len(self.wynik.tema.kolumny)+self.wynik.kolumnyCena.index(_kol)-1
                    worksheet.write(index+1,colIdx,cena, cf)
                    
        self.writer.close()

