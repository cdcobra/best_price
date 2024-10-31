import os,json

#liczba
def liczba(x):
    try:        
        return round(float(x),2)
    except:
        print(x)
    return 0

def szukajKol(lista,plik,nazwaKolumny):    
    os.system('cls')
    txt = f'Dla pliku {plik} wybierz numer kolumny z {nazwaKolumny}:'
    print(txt)
    for (index, kolumna) in enumerate(lista, start=0):
        print(index, ': ', kolumna)
    return lista[int(input(txt))]

def naEkran(txt):
    os.system('cls')
    print(f'{txt}')

def szukajPlik(wylaczenia,txt):
    os.system('cls')
    for (indeks,plik) in enumerate(os.listdir("."), start=0):
        if (plik.endswith(".xlsx") or plik.endswith(".xls")) and plik not in wylaczenia: 
            print(f'{indeks}: {plik}')
    return os.listdir(".")[int(input(txt))]

def setting():
    if not os.path.isfile('setting.json'):
        default()
    with open('setting.json', 'r') as file:
        return json.load(file)

def default():
    default = {
        "plikTema": "tema.xlsx",
        "plikWyniku": "wynik.xlsx",
        "kolumnyEan": ["Paskowy","Ean","EAN","kodPask"],
        "kolumnyCena": ["oferta","cena_prop","Cena sprzedaży netto"],
        "kolumnyDodatkowe": ["KodWlasny","NazwaZnacznika","Nazwa","IloscNaMagazynie"]
    }
    out_file = open("setting.json", "w")
    json.dump(default, out_file, ensure_ascii=False, indent=4)
    out_file.close()    