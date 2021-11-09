from django.forms import ModelForm
from django import forms

from hotel_pour_animal.models.animal import OuiNonChoice, EmplacementChoice, Animal

from dal import autocomplete


class AnimalBaseForm:
    def clean(self):

        cleaned_data = ModelForm.clean(self)

        vaccine = cleaned_data.get('vaccine')

        if vaccine == OuiNonChoice.OUI.name:
            date_vaccin = cleaned_data.get('date_dernier_vaccin')
            if not date_vaccin:
                msg = (
                    "Comme l'animal est vacciné, veuillez obligatoirement "
                    "indiquer la date du dernier vaccin"
                )
                self._errors['date_dernier_vaccin'] = self.error_class([msg])
                del cleaned_data['date_dernier_vaccin']

        sterilise = cleaned_data.get('sterilise')

        if sterilise == OuiNonChoice.OUI.name:
            date_sterilisation = cleaned_data.get('date_sterilisation')
            if not date_sterilisation:
                msg = (
                    "Comme l'animal est stérilisé, veuillez obligatoirement"
                    "indiquer la date de stérilisation"
                )
                self._errors['date_sterilisation'] = self.error_class([msg])
                del cleaned_data['date_sterilisation']

        emplacement = cleaned_data.get('emplacement')

        # si l'animal est inscrit en pension, il doit avoir un propriétaire
        if emplacement == EmplacementChoice.PENSION.name:
            if not cleaned_data.get('proprietaire'):
                msg = "Pour un animal inscrit en pension, veuillez obligatoirement indiquer un proprétaire"
                self._errors['proprietaire'] = self.error_class([msg])
                del cleaned_data['proprietaire']
        # si l'animal arrive au refuge, on doit indiquer sa date d'arrivée et il n'a pas de propriétaire
        elif emplacement == EmplacementChoice.REFUGE.name:
            if not cleaned_data.get('date_arrivee'):
                msg = "Veuillez indiquer obligatoirement la date d'arrivée de l'animal au refuge"
                self._errors['date_arrivee'] = self.error_class([msg])
                del cleaned_data['date_arrivee']
            if cleaned_data.get('proprietaire'):
                msg = "Si l'animal arrive au refuge, il n'a pas de propriétaire"
                self._errors['proprietaire'] = self.error_class([msg])
                del cleaned_data['proprietaire']

        return cleaned_data


class DateInput(forms.DateInput):
    input_type = 'date'


class AnimalCreateForm(AnimalBaseForm, ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Animal
        fields = (
            'nom',
            'type_animal',
            'emplacement',
            'sexe',
            'description',
            'date_naissance',
            'date_arrivee',
            'sterilise',
            'date_sterilisation',
            'vaccine',
            'date_dernier_vaccin',
            'proprietaire',
        )
        widgets = {
            'date_naissance': DateInput(),
            'date_arrivee': DateInput(),
            'date_sterilisation': DateInput(),
            'date_dernier_vaccin': DateInput(),
        }
        # widgets = {
        #     'proprietaire': autocomplete.ModelSelect2(url='personne_autocomplete'),
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date_naissance'].widget.attrs['class'] = 'datePicker'
    #     self.fields['date_arrivee'].widget.attrs['class'] = 'datePicker'
    #     self.fields['date_sterilisation'].widget.attrs['class'] = 'datePicker'
    #     self.fields['date_dernier_vaccin'].widget.attrs['class'] = 'datePicker'


