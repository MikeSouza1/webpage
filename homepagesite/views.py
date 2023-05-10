from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'site_title': 'Página Inicial - '
    }

    return render(request, 'global/base.html', context,)
