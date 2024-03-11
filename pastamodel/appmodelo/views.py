from django.shortcuts import render
from appmodelo.models importComentario

def index (request):
lista_itens = Comentario.objects.all()
return render (request, 'index.html', {'lista_itens':lista_itens})
