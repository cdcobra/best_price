import os

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
    return [lista[int(input(txt))]]

def naEkran(txt):
    os.system('cls')
    print(f'{txt}')
    