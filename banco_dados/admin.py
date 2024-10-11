from django.contrib import admin

# Register your models here.
from .models import Usuario, Inscricao, Edital, BolsistaValidado, Convocacao, Posse, DadosBancarios, BolsistaAtivo, Frequencia, Registros, ConsultaPag 
admin.site.register(Usuario)
admin.site.register(Inscricao)
admin.site.register(Edital)
admin.site.register(BolsistaValidado)
admin.site.register(Convocacao)
admin.site.register(Posse)
admin.site.register(DadosBancarios)
admin.site.register(BolsistaAtivo)
admin.site.register(Frequencia)
admin.site.register(Registros)
admin.site.register(ConsultaPag)

