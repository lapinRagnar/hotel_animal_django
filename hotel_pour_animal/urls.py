from django.urls import path
from .views import home, personne


urlpatterns = [
    # path('', home.index, name='home'),

    # urls pour personne
    path('personnes', personne.personne_list, name='personnes'),


]