from django.forms import ModelForm
from hotel_pour_animal.models.personne import Personne


class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'prenom', 'email', 'adresse', 'code_postal', 'ville', 'telephone', 'commentaire')
