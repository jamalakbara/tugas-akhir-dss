import random
import pandas as pd
import os
import math

from .misc import open_tabel, getMean
from .weighting import start_weight as sw

from dss.settings import BASE_DIR

def add_parameter(nilai, tabel_alternatif):
    tabel_alternatif["Parameter"] = nilai
    
    return tabel_alternatif

def get_jurusan(tabel_alternatif):
    pilihan_jurusan = []
    for column in tabel_alternatif:
        if column != "Parameter":
            pilihan_jurusan.append(column)
            
    return pilihan_jurusan

def deviasi(tabel_alternatif, jurusan, jurusan_compare, index_name):
    nilai_deviasi = tabel_alternatif[jurusan][index_name] - tabel_alternatif[jurusan_compare][index_name]
    
    return nilai_deviasi

def idx_pref_global1(fp_gaussian, column_test, weight):
    index_preferensi_global = {}
    
    for column in fp_gaussian:
        nilai_gaussian = 0
        for kriteria in fp_gaussian.index:
        
            if column_test.casefold() == column.casefold().split("&")[0].replace(" (ips)", "")\
            or column_test.casefold() == column.casefold().split("&")[0].replace(" (ipa)", ""):
                nilai_gaussian += fp_gaussian[column][kriteria]
            else:
                nilai_gaussian += fp_gaussian[column][kriteria]*weight[kriteria]
            
        index_preferensi_global[column] = nilai_gaussian
        
    tabel_index_preferensi_global = pd.DataFrame(index_preferensi_global, index = ["Index Preferensi Global"])

    return tabel_index_preferensi_global

def idx_pref_global(fp_gaussian, weight):
    index_preferensi_global = {}
    
    for column in fp_gaussian:
        nilai_gaussian = 0
        for kriteria in fp_gaussian.index:
            nilai_gaussian += fp_gaussian[column][kriteria] * weight[kriteria]
            
        index_preferensi_global[column] = nilai_gaussian
        
    tabel_index_preferensi_global = pd.DataFrame(index_preferensi_global, index = ["Index Preferensi Global"])

    return tabel_index_preferensi_global

def entering_flow(pilihan_jurusan, index_preferensi_global):
    e_flow = {}

    for item in pilihan_jurusan:
        ef = 0
        for piece in index_preferensi_global:
            s = piece.split("&")

            if item in s and s.index(item) == 1:
                ef += index_preferensi_global[piece]["Index Preferensi Global"] * (1/(len(pilihan_jurusan) - 1))

        e_flow[item] = ef

    return e_flow

def leaving_flow(pilihan_jurusan, index_preferensi_global):
    l_flow = {}

    for item in pilihan_jurusan:
        lf = 0
        for piece in index_preferensi_global:
            s = piece.split("&")

            if item in s and s.index(item) == 0:
                lf += index_preferensi_global[piece]["Index Preferensi Global"] * (1/(len(pilihan_jurusan) - 1))

        l_flow[item] = lf

    return l_flow

def net_flow(pilihan_jurusan, e_flow, l_flow):
    n_flow = {}

    for jurusan in pilihan_jurusan:
        n_flow[jurusan] = l_flow[jurusan] - e_flow[jurusan]

    return n_flow
    
def get_std(tabel_alternatif):
    #nyari simpangan baku
    std = tabel_alternatif.std(axis=1)

    return std

def get_mean(tabel_alternatif):
    #nyari rata2
    mean = tabel_alternatif.mean(axis=1)

    return mean

def get_params(mean, nilai, std):
    params = []
    for bjg in range(len(nilai)):
        tot = (nilai[bjg]- mean[bjg]) / std[bjg]
        params.append(tot)

    return params

def fungsi_preferensi_gaussian(tabel_alternatif, pilihan_jurusan):
    fp_gaussian = {}
    fp_gaussian_val = list()
    tabel_gaus = pd.DataFrame()
    #adaw = {}

    for jurusan in pilihan_jurusan:
        for jurusan_compare in pilihan_jurusan:
            if jurusan == jurusan_compare:
                continue
            else:
                for index_name in tabel_alternatif.index:
                    if "(IPA)" in jurusan.split():
                        if index_name == "Matematika" or index_name == "Inggris" or index_name == "Indonesia" or index_name == "Fisika" or index_name == "Kimia" or index_name == "Biologi":

                               #menghitung deviasi
                            nilai_deviasi = deviasi(tabel_alternatif, jurusan, jurusan_compare, index_name)

                            #menghitung fungsi preferensi gaussian
                            if nilai_deviasi > 0:
                                gaussian = 1 - math.exp(-1*(((nilai_deviasi)**2) / (2*((tabel_alternatif["Parameter"][index_name])**2))))
                                #adaw[f"{jurusan}&{jurusan_compare} ({index_name})"] = nilai_deviasi
                            else:
                                gaussian = 0
                                #adaw[f"{jurusan}&{jurusan_compare} ({index_name})"] = nilai_deviasi

                            deviasi_name = f"{jurusan}&{jurusan_compare}"
                            fp_gaussian_val.append(gaussian)
                        else:
                            fp_gaussian_val.append(0)

                    elif "(IPS)" in jurusan.split():
                        if index_name == "Ekonomi" or index_name == "Inggris" or index_name == "Indonesia" or index_name == "Geografi" or index_name == "Sosiologi":

                            #menghitung deviasi
                            nilai_deviasi = deviasi(tabel_alternatif, jurusan, jurusan_compare, index_name)

                            #menghitung fungsi preferensi gaussian
                            if nilai_deviasi > 0:
                                gaussian = 1 - math.exp(-1*(((nilai_deviasi)**2) / (2*((tabel_alternatif["Parameter"][index_name])**2))))
                                #adaw[f"{jurusan}&{jurusan_compare} ({index_name})"] = nilai_deviasi
                            else:
                                gaussian = 0
                                #adaw[f"{jurusan}&{jurusan_compare} ({index_name})"] = nilai_deviasi

                            deviasi_name = f"{jurusan}&{jurusan_compare}"
                            fp_gaussian_val.append(gaussian)
                        else:
                            fp_gaussian_val.append(0)

                    try:
                        fp_gaussian[deviasi_name] = fp_gaussian_val
                        
                    except NameError:
                        continue
                        
            if tabel_gaus.empty:
                tabel_gaus = pd.DataFrame(fp_gaussian,[
                    "Matematika",
                    "Inggris",
                    "Indonesia",
                    "Fisika",
                    "Kimia",
                    "Biologi",
                    "Ekonomi",
                    "Geografi",
                    "Sosiologi",
                ])
            else:
                try:
                    tabel_gaus[deviasi_name] = fp_gaussian_val
                except ValueError:
                    continue
            fp_gaussian_val  = list()

    return tabel_gaus

def start_promethee():
    nilai = getMean() #Ambil nilai dari inputan

    tabel_alternatif = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Tabel Alternatif.csv')) #Buka tabel alternatif

    weight = sw(tabel_alternatif)

    mean = get_mean(tabel_alternatif) #Dapetin rata2 per kriteria
    std = get_std(tabel_alternatif) #Dapetin standar deviasi/simpangan baku
    params = get_params(mean, nilai, std) #Menghasilkan paramater untuk ditambahin ke tabel alternatif

    tabel_alternatif = add_parameter(params, tabel_alternatif) #Nambahin params ke tabel alternatif

    pilihan_jurusan = get_jurusan(tabel_alternatif)

    fp_gaussian = fungsi_preferensi_gaussian(tabel_alternatif, pilihan_jurusan) #Menghitung fungsi preferensi gaussian

    index_preferensi_global = idx_pref_global(fp_gaussian, weight) #Menghitung index preferensi global

    e_flow = entering_flow(pilihan_jurusan, index_preferensi_global) #Menghitung entering flow

    l_flow = leaving_flow(pilihan_jurusan, index_preferensi_global) #Menghitung leaving flow

    n_flow = net_flow(pilihan_jurusan, e_flow, l_flow) #Menghitung net flow

    hasil_outrank = sorted(n_flow.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

    tab = dict()

    rank = list()
    jurusan = list()
    net = list()

    for i in range(len(hasil_outrank)):
        rank.append(i+1)
        jurusan.append(hasil_outrank[i][0])
        net.append(hasil_outrank[i][1])
        
    tab["Jurusan"] = jurusan
    tab["Net Flow"] = net

    tabel_hasil = pd.DataFrame(tab, index=rank)

    return tabel_hasil

def akurasi():
    nilai_test = pd.read_csv(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Splitted Test.csv'), index_col = 0)

    tabel_alternatif = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Tabel Alternatif.csv')) #Buka tabel alternatif

    weight = sw(tabel_alternatif)

    pilihan_jurusan = get_jurusan(tabel_alternatif)

    mean = get_mean(tabel_alternatif)
    std = get_std(tabel_alternatif)

    bener = 0
    listBener = list()
    for test_index in nilai_test.index:
    #assign nilai IPA/IPS
        try:
            if nilai_test["Jurusan Sekolah"][test_index].casefold() == "ipa":
                nilai = [
                    nilai_test["Rata-rata Matematika"][test_index],
                    nilai_test["Rata-rata Inggris"][test_index],
                    nilai_test["Rata-rata Indonesia"][test_index],
                    nilai_test["Rata-rata Fisika"][test_index],
                    nilai_test["Rata-rata Kimia"][test_index],
                    nilai_test["Rata-rata Biologi"][test_index],
                    0,
                    0,
                    0,
                ]
            elif nilai_test["Jurusan Sekolah"][test_index].casefold() == "ips":
                nilai = [
                    0,
                    nilai_test["Rata-rata Inggris"][test_index],
                    nilai_test["Rata-rata Indonesia"][test_index],
                    0,
                    0,
                    0,
                    nilai_test["Rata-rata Ekonomi"][test_index],
                    nilai_test["Rata-rata Geografi"][test_index],
                    nilai_test["Rata-rata Sosiologi"][test_index],
                ]
        except AttributeError:
            continue

        #Mendapatkan nilai2 parameter yang hendak digunakan
        params = get_params(mean, nilai, std)

        #Menambahkan kolom parameter ke tabel_alternatif
        tabel_alternatif = add_parameter(params, tabel_alternatif)

        #Mencari nilai fungsi preferensi gaussian
        fp_gaussian = fungsi_preferensi_gaussian(tabel_alternatif, pilihan_jurusan)

        #Menghitung index preferensi global
        index_preferensi_global = idx_pref_global1(fp_gaussian, f'{nilai_test["Jurusan Diterima"][test_index]} - {nilai_test["PTN Diterima"][test_index]}',weight)

        #Menghitung entering flow
        e_flow = entering_flow(pilihan_jurusan, index_preferensi_global)

        #Menghitung leaving flow
        l_flow = leaving_flow(pilihan_jurusan, index_preferensi_global)

        #Menghitung net flow
        n_flow = net_flow(pilihan_jurusan, e_flow, l_flow)

        #Mendapatkan Hasil Outrank
        hasil_outrank = sorted(n_flow.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

        tab = dict()

        rank = list()
        jurusan = list()
        net = list()

        for i in range(len(hasil_outrank)):
            rank.append(i+1)
            jurusan.append(hasil_outrank[i][0])
            net.append(hasil_outrank[i][1])

        tab["Jurusan"] = jurusan
        tab["Net Flow"] = net

        tabel_hasil = pd.DataFrame(tab, index=rank)
        listBener.append((tabel_hasil["Jurusan"][1], f'{nilai_test["Jurusan Diterima"][test_index]} - {nilai_test["PTN Diterima"][test_index]}'))

    dictBener = {
        "tebakan": [listBener[i][0] for i in range(len(listBener))],
        "asli": [listBener[i][1] for i in range(len(listBener))],
    }

    dfbener = pd.DataFrame(dictBener)

    dfbener.to_csv(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar.csv'))