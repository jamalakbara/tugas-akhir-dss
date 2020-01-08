from .misc import open_tabel

import numpy as np
import math

def calc_miu_v(tabel_alternatif):

    row = list()
    for index in tabel_alternatif.index:
        row_val = list()
        for column in tabel_alternatif:
            #derajat kepemilikan
            miu_x = tabel_alternatif[column][index]/100
            #derajat ketidakpemilikan
            v_x = 1-miu_x

            row_val.append([miu_x,v_x])

        row.append(row_val)

    return row

def entropy_mtrx(decision_matrix):
    entropy_matrix = np.zeros(shape=(9,137))

    for i in range(len(decision_matrix)):
        for idx, val in enumerate(decision_matrix[i]):
            entropy = 1-abs(val[0]-val[1])
            entropy_matrix[i][idx] = entropy

    return entropy_matrix

def knowledge_measure(decision_matrix, entropy_matrix):
    for i in range(len(entropy_matrix)):
        for idx, val in enumerate(entropy_matrix[0]):
            entropy_matrix[i][idx] = 1 - 0.5*(val+(1 - decision_matrix[i][idx][0] - decision_matrix[i][idx][1]))
    
    return entropy_matrix

def hitung_a(entropy_matrix):
    a = list()
    for index in range(len(entropy_matrix)):
        a_val = 0
        for j, val in enumerate(entropy_matrix[index]):
            if not math.isnan(val):
                a_val += val

        a.append(a_val)

    return a

def hitung_weight(a, weight):
    for i, val in enumerate(a):
        if i == 0:
            weight["Matematika"] = val/sum(a)
        elif i == 1:
            weight["Inggris"] = val/sum(a)
        elif i == 2:
            weight["Indonesia"] = val/sum(a)
        elif i == 3:
            weight["Fisika"] = val/sum(a)
        elif i == 4:
            weight["Kimia"] = val/sum(a)
        elif i == 5:
            weight["Biologi"] = val/sum(a)
        elif i == 6:
            weight["Ekonomi"] = val/sum(a)
        elif i == 7:
            weight["Geografi"] = val/sum(a)
        elif i == 8:
            weight["Sosiologi"] = val/sum(a)
            
    return weight

def start_weight(tabel_alternatif):
    weight = {
        "Matematika": 0,
        "Inggris": 0,
        "Indonesia": 0,
        "Fisika": 0,
        "Kimia": 0,
        "Biologi": 0,
        "Ekonomi": 0,
        "Geografi": 0,
        "Sosiologi": 0,
    }

    miu_v = calc_miu_v(tabel_alternatif) #Mengihtung derajat kepemilikan dan derajat ketidakpemilikan

    decision_matrix = np.array([miu_v[i] for i in range(len(miu_v))]) #bikin decision matriks

    entropy_matrix = entropy_mtrx(decision_matrix) #Bikin entropy matrix

    knowledge_measure_matrix = knowledge_measure(decision_matrix, entropy_matrix) #bikin knowledge matrix

    a = hitung_a(knowledge_measure_matrix) #menghitung a

    weight = hitung_weight(a, weight)

    return weight
