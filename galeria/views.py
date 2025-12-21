from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia  

def index(request):

    fotografias = Fotografia.objects.order_by("data_publicacao").filter(publicada=True)#busca os objetos do modelo Fotografia que estão publicados
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #PK = primary key
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    render(request, "galeria/buscar.html")