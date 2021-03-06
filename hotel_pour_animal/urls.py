from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from hotel_pour_animal.models.personne import Personne

from .views import home, personne, animal
from .views.personne import PersonneAutocomplete

urlpatterns = [
    # path('', home.index, name='home'),

    # urls pour personne
    path('personnes', personne.personne_list, name='personnes'),
    path('personnes/create', personne.CreatePerson.as_view(), name='create_personne'),
    path('personnes/update/<int:pk>/', personne.UpdatePerson.as_view(), name='update_personne'),
    path('personnes/<int:pk>/', login_required(DetailView.as_view(
        model=Personne,
        template_name="hotel_pour_animal/personne/personne_detail.html"
    )), name='detail_personne'),
    path('personnes/autocomplete/', login_required(PersonneAutocomplete.as_view()), name='personne_autocomplete'),

    # animaux
    path('animaux', animal.animal_list, name='animaux'),
    path('animaux/create', animal.CreateAnimal.as_view(), name='create_animal'),

]
