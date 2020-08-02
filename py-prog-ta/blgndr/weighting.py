#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getDecisionMatrix(tabel_alternatif):
    #mentraspose tabel alternatif agar
    decision_matrix = tabel_alternatif.transpose(copy=True)
    #membuat decision matrix
    for kriteria in decision_matrix.columns:
        decision_matrix[kriteria] = decision_matrix[kriteria].astype(object)
    else:
        for alternatif in decision_matrix.index:
            for kriteria in decision_matrix.columns:
                #menghasilkan derajat kepemilikan
                miu_x = decision_matrix.loc[alternatif, kriteria] / 100
                #menghasilkan derajat ketidakpemilikan
                v_x = 1 - miu_x
                decision_matrix.loc[alternatif, kriteria] = [miu_x,v_x]
                
    return decision_matrix


# In[ ]:


def getEntropyMatrix(decision_matrix):
    #meng-copy decision matrix kedalam variabel
    entropy_matrix = decision_matrix.copy()
    #membuat entropy matrix
    for alternatif in entropy_matrix.index:
        for kriteria in entropy_matrix.columns:
            entropy = 1 - abs(entropy_matrix.loc[alternatif, kriteria][0] - entropy_matrix.loc[alternatif, kriteria][1])
            entropy_matrix.loc[alternatif, kriteria] = entropy
    else:
        for kriteria in entropy_matrix.columns:
            entropy_matrix[kriteria] = entropy_matrix[kriteria].astype(float)
            
    return entropy_matrix


# In[ ]:


def getKnowledgeMatrix(entropy_matrix):
    #meng-copy entropy matrix ke dalam variabel
    knlowledge_matrix =  entropy_matrix.copy()
    #membuat knowledge matrix
    for alternatif in knlowledge_matrix.index:
        for kriteria in knlowledge_matrix.columns:
            knlowledge_matrix.loc[alternatif, kriteria] = 1 - 0.5*(knlowledge_matrix.loc[alternatif, kriteria])
            
    return knlowledge_matrix


# In[ ]:


def getWeight(knowledge_matrix):
    #menghitung a
    a = knowledge_matrix.sum()
    #menghitung sigma a
    sigma_a = a.sum()
    #mendapatkan weight
    weight = dict()
    for kriteria, val in a.items():
        weight_val = val / sigma_a
        weight[kriteria] = float("%.3f" % weight_val)
        
    return weight

