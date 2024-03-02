from django.contrib import admin
from .models import Photography

class PhotographyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'published']
    list_display_links = ['id', 'name']
    list_editable = ['published', ]
    list_per_page = 10
    
admin.site.register(Photography, PhotographyAdmin)
