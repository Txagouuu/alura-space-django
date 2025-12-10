from django.contrib import admin
from galeria.models import Fotografia

 #classe para personalizar a exibição no admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome','categoria')#necessario colocar uma viirgula no final para ser reconhecido como tupla
    list_per_page = 10

admin.site.register(Fotografia,ListandoFotografias)
