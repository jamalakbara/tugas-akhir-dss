from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dss-home"),
    path('input/', views.inputNilai, name="dss-input"),
    path('rekomendasi/', views.rekomendasiJurusan, name="dss-rekomendasi"),
    path('nilai/', views.nilaiSaya, name="dss-nilai"),
    path('akurasiSatu/', views.akurasiSatu, name="dss-akurasiSatu"),
    path('akurasiDua/', views.akurasiDua, name="dss-akurasiDua"),
    path('akurasiTiga/', views.akurasiTiga, name="dss-akurasiTiga"),
    path('dataTest/', views.dataTest, name="dss-dataTest"),
]
