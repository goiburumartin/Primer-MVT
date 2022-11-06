from django.shortcuts import render

from AppMvt.models import familiar1,familiar2,familiar3

# Create your views here.

def mostrar_familiares(request):

    f1 = familiar1(nombre = "Federico", apellido = "Serpa", edad = "18", nacimiento = "2003-5-14", experiencia = "[2016-2020]")
    f2 = familiar1(nombre = "Valentino", apellido = "Dinatale", edad = "19", nacimiento = "2002-10-21", experiencia = "[2015-2018]")
    f3 = familiar1(nombre = "Nicolas", apellido = "Ramirez", edad = "17", nacimiento = "2004-6-18", experiencia = "[2020-2021]")

    return render(request, "AppMvt/familia.html" , {"familiares":[f1,f2,f3]})