#sprawdz pliki
for plik in os.listdir("."):
    if (plik.endswith(".xlsx") or plik.endswith(".xls")) and plik not in [plikWynikowy, plikTema]:        
        #ładuje plik
        df = pd.read_excel(plik, sheet_name=0)
        
        #szukam kolumn
        colEan = [x for x in dictEan if x in df]
        colCena = [x for x in dictCena if x in df]
        
        #jeżeli nie znaleziono kolumny dla EAN
        if not colEan:            
            colEan = [f.szukajKol(df.columns.tolist(),plik,'EAN')]        

        #jeżeli nie znaleziono kolumny dla CENA
        if not colCena:
            colCena = [f.szukajKol(df.columns.tolist(),plik,'CENA')] 

        #jeżeli znaleziono
        if colEan and colCena:
            f.naEkran(f'Plik: {plik} Kolumna cena: {colCena[0]}, Kolumna EAN: {colEan[0]}')
            
            #dodaj nagłówek
            wynik[plik] = None
            kolumnyCena.append(plik)
            #sprawdz wg Tema
            for index, row in wynik.iterrows():
                find = df.index[df[colEan[0]]==row[plikTemaEan]].tolist()
                if find:
                    wynik.at[index, plik] = f.liczba(df.loc[find[0], colCena[0]])