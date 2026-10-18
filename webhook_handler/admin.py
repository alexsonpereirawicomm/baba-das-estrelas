from django.contrib import admin
from .models import Jogador, Baba, Convidado, ListaDeEspera

admin.site.register(Jogador)
admin.site.register(Baba)
admin.site.register(Convidado)
admin.site.register(ListaDeEspera)
