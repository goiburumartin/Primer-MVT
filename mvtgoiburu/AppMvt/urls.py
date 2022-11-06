from django.urls import path

from AppMvt.views import mostrar_familiares

urlpatterns = [
    path("" , mostrar_familiares)
]