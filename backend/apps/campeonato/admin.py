from django.contrib import admin

from .models import Campeonato, Jogo, Rodada, Classificacao

# Register your models here.
admin.site.register(Campeonato)
admin.site.register(Jogo)
admin.site.register(Rodada)
admin.site.register(Classificacao)
