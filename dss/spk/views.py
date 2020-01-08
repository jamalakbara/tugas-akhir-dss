from django.shortcuts import render

from .misc import *
from .promethee import start_promethee as sp, akurasi

import os

from dss.settings import BASE_DIR

# Create your views here.
def inputNilai(request):
    context =  {
        "title": "Input Nilai"
    }
    
    return render(request, 'spk/inputNilai.html', context)

def rekomendasiJurusan(request):
    context =  {
        "title": "Rekomendasi Jurusan"
    }
    
    if os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv')):
        hasil_outrank = sp()
        context["rekomendasi"] = [item for item in hasil_outrank["Jurusan"]]
    
    return render(request, 'spk/rekomendasiJurusan.html', context)

def nilaiSaya(request):
    context = {
        "title": "Nilai Saya",
    }

    if request.method == "POST":
        if request.POST["jurusan-sekolah"] == "IPA":
            dataNilai = {
                "Inggris": [float(request.POST["ing1"]), float(request.POST["ing1"]), float(request.POST["ing1"]), float(request.POST["ing1"]), float(request.POST["ing1"])],
                "Indonesia": [float(request.POST["ind1"]), float(request.POST["ind2"]), float(request.POST["ind3"]), float(request.POST["ind4"]), float(request.POST["ind5"])],
                "Matematika": [float(request.POST["mtk1"]), float(request.POST["mtk2"]), float(request.POST["mtk3"]), float(request.POST["mtk4"]), float(request.POST["mtk5"])],
                "Fisika": [float(request.POST["fsk1"]), float(request.POST["fsk2"]), float(request.POST["fsk3"]), float(request.POST["fsk4"]), float(request.POST["fsk5"])],
                "Kimia": [float(request.POST["kma1"]), float(request.POST["kma2"]), float(request.POST["kma3"]), float(request.POST["kma4"]), float(request.POST["kma5"])],
                "Biologi": [float(request.POST["blg1"]), float(request.POST["blg2"]), float(request.POST["blg3"]), float(request.POST["blg4"]), float(request.POST["blg5"])],
            }
        else:
            dataNilai = {
                "Inggris": [float(request.POST["ingg1"]), float(request.POST["ingg2"]), float(request.POST["ingg3"]), float(request.POST["ingg4"]), float(request.POST["ingg5"])],
                "Indonesia": [float(request.POST["indo1"]), float(request.POST["indo2"]), float(request.POST["indo3"]), float(request.POST["indo4"]), float(request.POST["indo5"])],
                "Ekonomi": [float(request.POST["ekn1"]), float(request.POST["ekn2"]), float(request.POST["ekn3"]), float(request.POST["ekn4"]), float(request.POST["ekn5"])],
                "Geografi": [float(request.POST["ggr1"]), float(request.POST["ggr2"]), float(request.POST["ggr3"]), float(request.POST["ggr4"]), float(request.POST["ggr5"])],
                "Sosiologi": [float(request.POST["ssl1"]), float(request.POST["ssl2"]), float(request.POST["ssl3"]), float(request.POST["ssl4"]), float(request.POST["ssl5"])],
            }
        exportNilai(dataNilai)

    if os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv')):
        nilai = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv'))
        try:
            nilai["Matematika"]
        except KeyError:
            context['ekonomi'] = [item for item in nilai['Ekonomi']]
            context['geografi'] = [item for item in nilai['Geografi']]
            context['sosiologi'] = [item for item in nilai['Sosiologi']]
        else:
            context['matematika'] = [item for item in nilai['Matematika']]
            context['fisika'] = [item for item in nilai['Fisika']]
            context['kimia'] = [item for item in nilai['Kimia']]
            context['biologi'] = [item for item in nilai['Biologi']]
        finally:
            context['inggris'] = [item for item in nilai['Inggris']]
            context['indonesia'] = [item for item in nilai['Indonesia']]
    return render(request, 'spk/nilaiSaya.html', context)

def notifikasi(request):
    context =  {
        "title": "Notifikasi"
    }

    return render(request, 'spk/notifications.html', context)

def dashboard(request):
    context =  {
        "title": "Dashboard"
    }

    if os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv')):
        nilai = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'nilai.csv'))
        try:
            nilai["Matematika"]
        except KeyError:
            context['ekonomi'] = [item for item in nilai['Ekonomi']]
            context['geografi'] = [item for item in nilai['Geografi']]
            context['sosiologi'] = [item for item in nilai['Sosiologi']]
        else:
            context['matematika'] = [item for item in nilai['Matematika']]
            context['fisika'] = [item for item in nilai['Fisika']]
            context['kimia'] = [item for item in nilai['Kimia']]
            context['biologi'] = [item for item in nilai['Biologi']]
        finally:
            context['inggris'] = [item for item in nilai['Inggris']]
            context['indonesia'] = [item for item in nilai['Indonesia']]

    return render(request, 'spk/dashboard.html', context)

def akurasiSatu(request):
    context =  {
        "title": "Hasil Percobaan 1"
    }

    if not os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar.csv')):
        akurasi()
    else:
        hasilPrediksi = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi.csv'))
        hasilBenar = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar.csv'))
        dataTest = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Splitted Test.csv'))

        benar = [item for item in hasilBenar["tebakan"]]
        context["true_positive"] = len(benar)
        context["false_positive"] = len(hasilPrediksi) - context["true_positive"]
        context["true_negative"] = len(dataTest) - len(hasilPrediksi)
        context["false_negative"] = len(dataTest) - context["true_positive"] - context["true_negative"] - context["false_positive"]

        print(len(hasilPrediksi))

        # context["benar"] = [item for item in hasilBenar["tebakan"]]
        # context["asli"] = [item for item in hasilBenar["asli"]]
        context["dataTest"] = dataTest

    return render(request, 'spk/dashboard_akurasi.html', context)

def akurasiTiga(request):
    context =  {
        "title": "Hasil Percobaan 3"
    }

    if not os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar 10.csv')):
        akurasi()
    else:
        hasilPrediksi = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi 10 rank unk.csv'))
        hasilBenar = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar 10.csv'))
        dataTest = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Splitted Test.csv'))

        benar = [item for item in hasilBenar["tebakan"]]
        context["true_positive"] = len(benar)
        context["false_positive"] = len(hasilPrediksi) - context["true_positive"]
        context["true_negative"] = len(dataTest) - len(hasilPrediksi)
        context["false_negative"] = len(dataTest) - context["true_positive"] - context["true_negative"] - context["false_positive"]

        print(len(hasilPrediksi))

        # context["benar"] = [item for item in hasilBenar["tebakan"]]
        # context["asli"] = [item for item in hasilBenar["asli"]]
        context["dataTest"] = dataTest

    return render(request, 'spk/dashboard_akurasi.html', context)

def akurasiDua(request):
    context =  {
        "title": "Hasil Percobaan 2"
    }

    if not os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar 5.csv')):
        akurasi()
    else:
        hasilPrediksi = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi 5 rank unk.csv'))
        hasilBenar = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Hasil Prediksi Benar 5.csv'))
        dataTest = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Splitted Test.csv'))

        benar = [item for item in hasilBenar["tebakan"]]
        context["true_positive"] = len(benar)
        context["false_positive"] = len(hasilPrediksi) - context["true_positive"]
        context["true_negative"] = len(dataTest) - len(hasilPrediksi)
        context["false_negative"] = len(dataTest) - context["true_positive"] - context["true_negative"] - context["false_positive"]

        print(len(hasilPrediksi))

        # context["benar"] = [item for item in hasilBenar["tebakan"]]
        # context["asli"] = [item for item in hasilBenar["asli"]]
        context["dataTest"] = dataTest

    return render(request, 'spk/dashboard_akurasi.html', context)

def dataTest(request):
    context =  {
        "title": "Data Test"
    }

    if os.path.isfile(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Splitted Test.csv')):
        dataTest = open_tabel(os.path.join(BASE_DIR, 'spk\static\spk\data', 'Splitted Test.csv'))
        context["dataTest"] = dataTest.to_html()

    return render(request, 'spk/data_test.html', context)