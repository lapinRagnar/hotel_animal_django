from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from hotel_pour_animal.models.personne import Personne
from hotel_pour_animal.forms.personne import PersonneForm




@login_required
def personne_list(request):
    selected = 'personnes'
    personne_list = Personne.objects.all()


    # pagination - 10 éléments par page
    paginator = Paginator(personne_list.order_by('-date_mise_a_jour'), 10)

    print('----------->>> ', paginator)

    try:
        page = request.GET.get('page')
        if not page:
            page = 1
        personne_list = paginator.page(page)
    except EmptyPage:
        # si on dépasse la limite de pages, on prend la dernière
        personne_list = paginator.page(paginator.num_pages)

    return render(request, 'hotel_pour_animal/personne/personne_list.html', locals())


class CreatePerson(CreateView, LoginRequiredMixin):
    model = Personne
    form_class = PersonneForm
    template_name = 'hotel_pour_animal/personne/personne_form.html'

    def get_success_url(self):
        return reverse_lazy('detail_personne', kwargs={'pk': self.object.id})


class UpdatePerson(UpdateView, LoginRequiredMixin):
    model = Personne
    form_class = PersonneForm
    template_name = 'hotel_pour_animal/personne/personne_form.html'

    def get_success_url(self):
        return reverse_lazy('detail_personne', kwargs={'pk': self.object.id})


