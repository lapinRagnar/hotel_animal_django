from django.shortcuts import render


def index(request):
    return render(request, 'hotel_pour_animal/home.html', locals())

