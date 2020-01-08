import pandas as pd
import os

from dss.settings import BASE_DIR

def open_tabel(file):
    tabel = pd.read_csv(file, index_col=0)
    
    return tabel

def exportNilai(dataNilai):
    tabelNilai = pd.DataFrame(dataNilai, index=["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5"])

    if not os.path.exists(os.path.join(BASE_DIR, 'spk\static\spk\data')):
        os.mkdir(os.path.join(BASE_DIR, 'spk\static\spk\data'))

    tabelNilai.to_csv(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv'))

def getMean():
    nilai = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv'))
    
    avgNilai = nilai.mean(axis=0)
    
    nilaiSiswa = [val for val in avgNilai.values]

    try:
        print(nilai["Matematika"])
    except KeyError:
        for i in range(2,6):
            nilaiSiswa.insert(i,0)
    else:
        for i in range(0,3):
            nilaiSiswa.append(0)

    return nilaiSiswa

