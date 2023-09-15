from django.contrib import admin
from .models import Candidatos, Cidades, Urnas, Estado, ProcessoEleitoral


admin.site.site_header = "Sistema de Eleição Parametrizada"
admin.site.site_title = "Sistema de Eleição Parametrizada"
admin.site.index_title = "Sistema de Eleição Parametrizada"


class CadindatosAdmin(admin.ModelAdmin):
    list_display = ('numero_candidato', 'votos')


admin.site.register(Candidatos, CadindatosAdmin)


class CidadesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cidades, CidadesAdmin)


class UrnasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Urnas, UrnasAdmin)


class EstadoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Estado, EstadoAdmin)


class ProcessoEleitoralAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'is_valid')


admin.site.register(ProcessoEleitoral, ProcessoEleitoralAdmin)
