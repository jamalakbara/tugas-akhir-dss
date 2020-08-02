#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from .files import open_csv


# In[2]:


#anonymous function untuk dapetin nama2 mapel
getMapel = lambda columns: {column.split(" Semester ")[0] for column in columns if "Semester" in column}


# In[3]:


#anonymous function hitung rata2
avg = lambda list_nilai: sum(list_nilai) / len(list_nilai)


# In[5]:


def gantiPakeMedian(data):
    #mengambil nilai tengah dari tiap nilai
    data = data.replace("<70", 34.5)
    data = data.replace("71 - 75", 73)
    data = data.replace("76 - 80", 78)
    data = data.replace("81 - 85", 83)
    data = data.replace("86 - 90", 88)
    data = data.replace("91 - 95", 93)
    data = data.replace("> 95", 98)
    data = data.replace("No data", np.NaN)
    
    return data


# In[6]:


def getMeanLimaSemester(data, mata_pelajaran, index=0):
    #isi value untuk fillna
    values = dict()
    for i in range(1, 6):
        rata2_per_pelajaran = data[f"{mata_pelajaran} Semester {i}"].mean()
        values[f"{mata_pelajaran} Semester {i}"] = rata2_per_pelajaran

    #isi NaN dengan rata2 semester
    data = data.fillna(value=values)

    #itung rata2 nilai 5 semester
    nilai_siswa_5_semester_list = [data[f"{mata_pelajaran} Semester {idx}"][index] for idx in range(1,6)]
    rata2_nilai_siswa_5_semester = avg(nilai_siswa_5_semester_list)
            
    return rata2_nilai_siswa_5_semester


# In[7]:


def getJurusanDiterima(jurusan_diterima):
    if "administrasi" in jurusan_diterima.casefold()    or "sosial" in jurusan_diterima.casefold()    or "ekonomi" in jurusan_diterima.casefold()    or "hi" in jurusan_diterima.casefold()    or "hukum" in jurusan_diterima.casefold()    or "komunikasi" in jurusan_diterima.casefold()    or "politik" in jurusan_diterima.casefold()    or "sosiologi" in jurusan_diterima.casefold()    or "fsrd" in jurusan_diterima.casefold()    or "sbm" in jurusan_diterima.casefold()    or "akuntansi" in jurusan_diterima.casefold()    or "manajemen" in jurusan_diterima.casefold()    or "psdk" in jurusan_diterima.casefold()    or "fiskal" in jurusan_diterima.casefold()    or ("hubungan" in jurusan_diterima.casefold() and "internasional" in jurusan_diterima.casefold())    or "kriminologi" in jurusan_diterima.casefold()    or "psikologi" in jurusan_diterima.casefold()    or "bisnis" in jurusan_diterima.casefold()    or "filsafat" in jurusan_diterima.casefold()    or "jurnalistik" in jurusan_diterima.casefold()    or "humas" in jurusan_diterima.casefold()    or "desain" in jurusan_diterima.casefold()    or "film" in jurusan_diterima.casefold()    or "antropologi" in jurusan_diterima.casefold()    or "keluarga" in jurusan_diterima.casefold()    or "konsumen" in jurusan_diterima.casefold()    or "sejarah" in jurusan_diterima.casefold()    or "menejemen" in jurusan_diterima.casefold()    or "arkeologi" in jurusan_diterima.casefold()    or ("hubungan" in jurusan_diterima.casefold() and "masyarakat" in jurusan_diterima.casefold())    or "akutansi" in jurusan_diterima.casefold():
        jurusan_diterima = f"{jurusan_diterima} (IPS)"
    else:
        jurusan_diterima = f"{jurusan_diterima} (IPA)"

    return jurusan_diterima


# In[8]:


def getDictionary(data, mata_pelajaran):
    df = dict()
    df_train_test = dict()
    list_jurusan = set()
    indeks = 0
    for i, row in data.iterrows():
        #dapetin nama jurusan
        jrs = row["Jurusan Diterima"].strip()
        fkl = row["PTN Diterima"].strip()
        jurusan_diterima = f"{jrs} - {fkl}".upper()
        
        #dapetin nama jurusan
        jurusan_diterima = getJurusanDiterima(jurusan_diterima)
        
        if "sastra" not in jurusan_diterima.casefold()\
        and "bahasa" not in jurusan_diterima.casefold()\
        and "perpustakaan" not in jurusan_diterima.casefold()\
        and "ugm" not in jurusan_diterima.casefold():
            list_jurusan.add(jurusan_diterima)
            #masukkin nama panggilan
            if "Nama Panggilan" not in df_train_test:
                df_train_test["Nama Panggilan"] = [row["Nama Panggilan"]]
            else:
                df_train_test["Nama Panggilan"].append(row["Nama Panggilan"])
                
            #masukkin jurusan sekolah
            if "Jurusan Sekolah" not in df_train_test:
                df_train_test["Jurusan Sekolah"] = [row["Jurusan Sekolah"]]
            else:
                df_train_test["Jurusan Sekolah"].append(row["Jurusan Sekolah"])
            
            #masukkin pilihan
            if not pd.isnull(row["PTN Pilihan I"]) and row["PTN Pilihan I"].casefold() != "kosong":
                if "Pilihan I" not in df_train_test:
                    if not pd.isnull(row["Jurusan Pilihan I di PTN Pilihan I"]):
                        if row["Jurusan Pilihan I di PTN Pilihan I"].casefold() != "kosong" and row["Jurusan Pilihan I di PTN Pilihan I"].casefold() != "-":
                            pilihan = getJurusanDiterima(f"{row['Jurusan Pilihan I di PTN Pilihan I'].strip()} - {row['PTN Pilihan I'].strip()}")
                            df_train_test["Pilihan I"] = [pilihan.upper()]
                else:
                    if not pd.isnull(row["Jurusan Pilihan I di PTN Pilihan I"]):
                        if row["Jurusan Pilihan I di PTN Pilihan I"].casefold() != "kosong" and row["Jurusan Pilihan I di PTN Pilihan I"].casefold() != "-":
                            pilihan = getJurusanDiterima(f"{row['Jurusan Pilihan I di PTN Pilihan I'].strip()} - {row['PTN Pilihan I'].strip()}")
                            df_train_test["Pilihan I"].append(pilihan.upper())
                                                          
                if "Pilihan II" not in df_train_test:
                    if not pd.isnull(row["Jurusan Pilihan II di PTN Pilihan I"]):
                        if row["Jurusan Pilihan II di PTN Pilihan I"].casefold() != "kosong" and row["Jurusan Pilihan II di PTN Pilihan I"].casefold() != "-":
                            pilihan = getJurusanDiterima(f"{row['Jurusan Pilihan II di PTN Pilihan I'].strip()} - {row['PTN Pilihan I'].strip()}")
                            df_train_test["Pilihan II"] = [pilihan.upper()]
                        else:
                            df_train_test["Pilihan II"] = ["KOSONG"]
                    else:
                        if not pd.isnull(row["PTN Pilihan II"]):
                            if row["PTN Pilihan II"].casefold() != "kosong":
                                if not pd.isnull(row["Jurusan Pilihan I di PTN Pilihan II"]):
                                    if row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "kosong" and row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "-":
                                        pilihan = getJurusanDiterima(f'{row["Jurusan Pilihan I di PTN Pilihan II"].strip()} - {row["PTN Pilihan II"].strip()}')
                                        df_train_test["Pilihan II"] = [pilihan.upper()]
                                    else:
                                        df_train_test["Pilihan II"] = ["KOSONG"]
                                else:
                                    df_train_test["Pilihan II"] = ["KOSONG"]
                            else:
                                df_train_test["Pilihan II"] = ["KOSONG"]
                        else:
                            df_train_test["Pilihan II"] = ["KOSONG"]
                else:
                    if not pd.isnull(row["Jurusan Pilihan II di PTN Pilihan I"]):
                        if row["Jurusan Pilihan II di PTN Pilihan I"].casefold() != "kosong" and row["Jurusan Pilihan II di PTN Pilihan I"].casefold() != "-":
                            pilihan = getJurusanDiterima(f"{row['Jurusan Pilihan II di PTN Pilihan I'].strip()} - {row['PTN Pilihan I'].strip()}")
                            df_train_test["Pilihan II"].append(pilihan.upper())
                        else:
                            df_train_test["Pilihan II"].append("KOSONG")
                    else:
                        if not pd.isnull(row["PTN Pilihan II"]):
                            if row["PTN Pilihan II"].casefold() != "kosong" or row["PTN Pilihan II"].casefold() != "-":
                                if not pd.isnull(row["Jurusan Pilihan I di PTN Pilihan II"]):
                                    if row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "kosong" and row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "-":
                                        pilihan = getJurusanDiterima(f'{row["Jurusan Pilihan I di PTN Pilihan II"].strip()} - {row["PTN Pilihan II"].strip()}')
                                        df_train_test["Pilihan II"].append(pilihan.upper())
                                    else:
                                        df_train_test["Pilihan II"].append("KOSONG")
                                else:
                                    df_train_test["Pilihan II"].append("KOSONG")
                            else:
                                df_train_test["Pilihan II"].append("KOSONG")
                        else:
                            df_train_test["Pilihan II"].append("KOSONG")
                        
            if "Pilihan III" not in df_train_test:
                if not pd.isnull(row["PTN Pilihan II"]):
                    if row["PTN Pilihan II"].casefold() != "kosong" or row["PTN Pilihan II"].casefold() != "-":
                        if df_train_test["Pilihan II"][indeks].casefold() != getJurusanDiterima(f'{row["Jurusan Pilihan I di PTN Pilihan II"]} - {row["PTN Pilihan II"]}').casefold():
                            if not pd.isnull(row["Jurusan Pilihan I di PTN Pilihan II"]):
                                if row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "kosong" and row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "-":
                                    pilihan = getJurusanDiterima(f'{row["Jurusan Pilihan I di PTN Pilihan II"].strip()} - {row["PTN Pilihan II"].strip()}')
                                    df_train_test["Pilihan III"] = [pilihan.upper()]
                                else:
                                    df_train_test["Pilihan III"] = ["KOSONG"]
                            else:
                                df_train_test["Pilihan III"] = ["KOSONG"]
                        else:
                            if not pd.isnull(row["Jurusan Pilihan II di PTN Pilihan II"]):
                                if row["Jurusan Pilihan II di PTN Pilihan II"].casefold() != "kosong" and row["Jurusan Pilihan II di PTN Pilihan II"].casefold() != "-":
                                    pilihan = getJurusanDiterma(f'{row["Jurusan Pilihan II di PTN Pilihan II"].strip()} - {row["PTN Pilihan II"].strip()}')
                                    df_train_test["Pilihan III"] = [pilihan.upper()]
                                else:
                                    df_train_test["Pilihan III"] = ["KOSONG"]
                            else:
                                df_train_test["Pilihan III"] = ["KOSONG"]
                    else:
                        df_train_test["Pilihan III"] = ["KOSONG"]
                else:
                    df_train_test["Pilihan III"] = ["KOSONG"]
            else:
                if not pd.isnull(row["PTN Pilihan II"]):
                    if row["PTN Pilihan II"].casefold() != "kosong" or row["PTN Pilihan II"].casefold() != "-":
                        if df_train_test["Pilihan II"][indeks].casefold() != getJurusanDiterima(f'{row["Jurusan Pilihan I di PTN Pilihan II"]} - {row["PTN Pilihan II"]}').casefold():
                            if not pd.isnull(row["Jurusan Pilihan I di PTN Pilihan II"]):
                                if row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "kosong" and row["Jurusan Pilihan I di PTN Pilihan II"].casefold() != "-":
                                    pilihan = getJurusanDiterima(f'{row["Jurusan Pilihan I di PTN Pilihan II"].strip()} - {row["PTN Pilihan II"].strip()}')
                                    df_train_test["Pilihan III"].append(pilihan.upper())
                                else:
                                    df_train_test["Pilihan III"].append("KOSONG")
                            else:
                                df_train_test["Pilihan III"].append("KOSONG")
                        else:
                            if not pd.isnull(row["Jurusan Pilihan II di PTN Pilihan II"]):
                                if row["Jurusan Pilihan II di PTN Pilihan II"].casefold() != "kosong" and row["Jurusan Pilihan II di PTN Pilihan II"].casefold() != "-":
                                    pilihan = getJurusanDiterima(f'{row["Jurusan Pilihan II di PTN Pilihan II"].strip()} - {row["PTN Pilihan II"].strip()}')
                                    df_train_test["Pilihan III"].append(pilihan.upper())
                                else:
                                    df_train_test["Pilihan III"].append("KOSONG")
                            else:
                                df_train_test["Pilihan III"].append("KOSONG")
                    else:
                        df_train_test["Pilihan III"].append("KOSONG")
                else:
                    df_train_test["Pilihan III"].append("KOSONG")
            
            indeks += 1
                                                                        
            #masukkin jurusan diterima
            if "Jurusan Diterima" not in df_train_test:
                df_train_test["Jurusan Diterima"] = [jurusan_diterima]
            else:
                df_train_test["Jurusan Diterima"].append(jurusan_diterima)
        
            #bikin dictionary untuk data frame
            mean_list_temp = list()
            for item in mata_pelajaran:
                #masukkin mata pelajaran
                if item not in df_train_test:
                    df_train_test[item] = [getMeanLimaSemester(data, item, i)]
                else: 
                    df_train_test[item].append(getMeanLimaSemester(data, item, i))
                    
                if jurusan_diterima not in df:
                    df[jurusan_diterima] = [[getMeanLimaSemester(data, item, i)]]
                else:
                    if len(df[jurusan_diterima][0]) >= 9:
                        mean_list_temp.append(getMeanLimaSemester(data, item, i))
                        if len(mean_list_temp) >= 9:
                            df[jurusan_diterima].append(mean_list_temp)
                            del mean_list_temp
                    else:
                        df[jurusan_diterima][0].append(getMeanLimaSemester(data, item, i))

    #rata2in value di dictionary
    for item in list_jurusan:
        if len(df[item]) > 1:
            df[item] = [sum(x)/len(df[item]) for x in zip(*df[item])]
        else:
            df[item] = df[item][0]
    
                                                                            
    return [df, df_train_test]


# In[12]:


def clean():
    datasets = [
        "data/Data SNMPTN 2016 UI by @halokampus.csv",
        "data/Data SNMPTN 2017 UI by @halokampus.csv",
        "data/Data SNMPTN 2016 UNPAD by @halokampus.csv",
        "data/Data SNMPTN 2017 UNPAD by @halokampus.csv",
        "data/Data SNMPTN 2016 UNAIR by @halokampus.csv",
        "data/Data SNMPTN 2017 UNAIR by @halokampus.csv",
    ]

    #buka data terus masukkin ke list
    list_data = list()
    for data in datasets:
        list_data.append(open_csv(data))
    else:
        data = pd.concat(list_data, ignore_index=True)
        data = gantiPakeMedian(data)

    #dapetin mata pelajaran
    mata_pelajaran = getMapel(data)
    
    #dapetin dataframe dictionary untuk table alternatif
    df_table = getDictionary(data, mata_pelajaran)[0]
    
    #dapetin dataframe dictionary untuk test train
    df_test_train = getDictionary(data, mata_pelajaran)[1]
            
    #bikin tabel alternatif
    table_alternatif = pd.DataFrame(df_table, list(mata_pelajaran))
    
    #bikin test dan train
    train = pd.DataFrame(df_test_train)
    
    #train to csv
    train.to_csv("data/train-test/Splitted Train.csv", encoding="utf-8")
    
    #test to csv
    test = train.copy()
    test = test.sample(frac=0.3)
    test.to_csv("data/train-test/Splitted Test.csv", encoding="utf-8")
    
    return table_alternatif

