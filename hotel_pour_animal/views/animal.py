from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from hotel_pour_animal.forms.animal import AnimalCreateForm
from hotel_pour_animal.models.animal import Animal


@login_required
def animal_list(request):
    selected = 'animaux'
    animal_list = Animal.objects.all()

    paginator = Paginator(animal_list.order_by('-date_mise_a_jour'), 10)
    try:
        page = request.GET.get('page')
        if not page:
            page = 1
        animal_list = paginator.page(page)
    except EmptyPage:
        personnes = paginator.page(paginator.num_pages())

    return render(request, "hotel_pour_animal/animal/animal_list.html", locals())


class CreateAnimal(LoginRequiredMixin, CreateView):
    model = Animal
    form_class = AnimalCreateForm
    template_name = 'hotel_pour_animal/animal/animal_form.html'

    def get_success_url(self):
        return reverse_lazy('animaux')


