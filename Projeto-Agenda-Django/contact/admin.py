from django.contrib import admin

from contact import models

# Register your models here.

@admin.register(models.Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id', #ordem inversar do id
    list_filter = 'created_date', #filtro por data
    search_fields = 'id', 'first_name', 'last_name', #inserir busca
    list_per_page = 10 #páginação de contatos
    list_max_show_all = 200 #máximo a ser mostrado para todos os dados
    list_editable = 'first_name', 'last_name', #preferências de edição
    list_display_links = 'id', 'phone', #links de acesso ao contato específico