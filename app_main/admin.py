from django.contrib import admin
from .models import Category, Co
from import_export.admin import ImportExportModelAdmin

admin.site.register(Co)

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'old_price', 'new_price', 'rating', 'is_sale', 'created_at', 'updated_at')
    list_filter = ('is_sale', 'rating', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    list_editable = ('old_price', 'new_price', 'is_sale', 'rating')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Narx va Chegirma', {
            'fields': ('old_price', 'new_price', 'is_sale'),
            'classes': ('collapse',)
        }),
        ('Reyting', {
            'fields': ('rating',),
            'classes': ('wide',)
        }),
        ('Rasm', {
            'fields': ('image',)
        }),
        ('Vaqt Malumotlari', {
        'fields': ('created_at', 'updated_at'),
        'classes': ('collapse',)
    }),
    )
    readonly_fields = ('created_at', 'updated_at')


    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
admin.site.register(Category, CategoryAdmin)
