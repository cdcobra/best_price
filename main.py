import os
from excel import Excel

#przygotuj excel
excel =  Excel()

#otwórz na koniec
os.startfile(excel.setting['plikWyniku'])

# pip install auto-py-to-exe
# python -m auto_py_to_exe