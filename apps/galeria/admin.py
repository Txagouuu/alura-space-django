from django.contrib import admin
from apps.galeria.models import Fotografia

 #classe para personalizar a exibição no admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)#necessario colocar uma viirgula no final para ser reconhecido como tupla
    list_filter = ('categoria', "usuario")#necessario colocar uma viirgula no final para ser reconhecido como tupla
    list_editable = ('publicada',) #permite editar diretamente no admin
    list_per_page = 10


admin.site.register(Fotografia,ListandoFotografias)
