#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Usuario
from .models import Inscricao
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse("dudoca")

def usuários(request):
    Usuario_list = Usuario.objects.all()
    template = loader.get_template ("banco_dados/usuários.html")
    context = {
        "Usuario_list" : Usuario_list
    }
    #return render(request, "banco_dados/usuários.html", context)
    return HttpResponse(template.render(context,request))

# Leave the rest of the views (usuários, results, vote) unchanged

def details(request):
    Inscricao_list = Inscricao.objects.all()
    template = loader.get_template ("banco_dados/details.html")
    context = {
        "Inscricao_list" : Inscricao_list
    }
    #return render(request, "banco_dados/details.html", context)
    return HttpResponse(template.render(context,request))

# Leave the rest of the views (details, results, vote) unchanged
