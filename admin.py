from django.contrib import admin


@admin.register
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nome_empresa', 'categoria_empresa', 'quitado')


@admin.register
class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'valor')
