from django.forms import ModelForm, Form, CharField
from hotel_pour_animal.models.personne import Personne


class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'prenom', 'email', 'adresse', 'code_postal', 'ville', 'telephone', 'commentaire')


class PersonneSearchForm(Form):
    nom = CharField(max_length=100, required=False)
    prenom = CharField(max_length=100, required=False)
    email = CharField(max_length=100, required=False)

