from django.contrib import admin

# Register your models here.
from .models import usuario, inscricao, edital, bolsista_validado, convocacao, posse, dado_bancario, bolsista_ativo, frequencia, registro, consultapag 
admin.site.register(usuario)
admin.site.register(inscricao)
admin.site.register(edital)
admin.site.register(bolsista_validado)
admin.site.register(convocacao)
admin.site.register(posse)
admin.site.register(dado_bancario)
admin.site.register(bolsista_ativo)
admin.site.register(frequencia)
admin.site.register(registro)
admin.site.register(consultapag)

