from django.shortcuts import render

from apps.models import Person


def index(request):
    image = Person.objects.all()
    context = {
        'photos': image

    }
    return render(request, 'apps/index.html', context)
