import pandas as pd
import os
import xlsxwriter

#zmienne
plikWynikowy = 'wynik.xlsx'
plikTema = 'tema.xlsx'
plikTemaEan = 'Paskowy'
plikTemaCenaZakupu = 'CenaZakupuNetto'
kolumny = ['KodWlasny',plikTemaEan, 'NazwaZnacznika','Nazwa','IloscNaMagazynie',plikTemaCenaZakupu]
kolumnyCena = [plikTemaCenaZakupu]
dictEan = ['ean','EAN','kodPask']
dictCena = ['cena','oferta','cena_prop','Cena sprzedaży netto']

#liczba
def liczba(x):
    try:        
        return round(float(x),2)
    except:
        print(x)
    return 0

#przygotowanie DataFrame
wynik = pd.DataFrame(columns=kolumny)

#pobierz dane z Tema
print('Pobieram dane z Tema')
tema = pd.read_excel("tema.xlsx", sheet_name=0)
tema.dropna(subset=["Paskowy"], inplace=True)

#kopiowanie kolumn
for kol in kolumny:
    if kol in tema:
        wynik[kol] = tema[kol]
#print(wynik.dtypes)

#sprawdz pliki
for plik in os.listdir("."):
    if (plik.endswith(".xlsx") or plik.endswith(".xls")) and plik not in [plikWynikowy, plikTema]:        
        #ładuje plik
        df = pd.read_excel(plik, sheet_name=0)
        
        #szukam kolumn
        colEan = [x for x in dictEan if x in df]
        colCena = [x for x in dictCena if x in df]
        
        #jeżeli znaleziono
        if colEan and colCena:
            print('Znalazłem plik:',plik, ' Kolumna cena: ',colCena[0], 'Kolumna EAN:', colEan[0])
            #print(df.dtypes)
            
            #dodaj nagłówek
            wynik[plik] = None
            kolumnyCena.append(plik)
            #sprawdz wg Tema
            for index, row in wynik.iterrows():
                find = df.index[df[colEan[0]]==row[plikTemaEan]].tolist()
                if find:
                    wynik.at[index, plik] = liczba(df.loc[find[0], colCena[0]])
        else: 
            print('Znalazłem plik:',plik, ' ale nie mogę zlokalizować column dla EAN i/lub ceny')

#sortuj i wykop
wynik = wynik.sort_values(['NazwaZnacznika','Nazwa'], ignore_index=True)

#formatuj
writer = pd.ExcelWriter(plikWynikowy, engine='xlsxwriter', datetime_format='dd.mm.yyyy hh:mm:ss', date_format='dd.mm.yyyy')
wynik.to_excel(writer, index=False)
workbook  = writer.book
worksheet = writer.sheets["Sheet1"]
(max_row, max_col) = wynik.shape
worksheet.set_column(0,  max_col - 1, 12)
worksheet.autofilter(0, 0, max_row, max_col - 1)
worksheet.autofit()
worksheet.freeze_panes(1, 0)

#koloruj najlepsze ceny
cf = workbook.add_format({'bg_color': '#4FFF33'})
# print(wynik[kolumnyCena].idxmin(axis="columns").items()))
# for index, best in wynik[kolumnyCena].idxmin(axis="columns").items():
#     print(index, best, wynik.loc[wynik.index[index], best])
#     colIdx = len(kolumny)+kolumnyCena.index(best)-1
#     worksheet.write(index,colIdx,best, cf)
for index,row in wynik.iterrows():    
    cena = min(filter(None,row[kolumnyCena].tolist()), default=0)
    for _kol in kolumnyCena:
        if(cena==row[_kol]):
            colIdx = len(kolumny)+kolumnyCena.index(_kol)-1
            worksheet.write(index+1,colIdx,cena, cf)
            
writer.close()

#otwórz na koniec
os.startfile(plikWynikowy)

#poczekaj na zakończenie
input("Enter by zakończyć")

# pip install auto-py-to-exe
# python -m auto_py_to_exe