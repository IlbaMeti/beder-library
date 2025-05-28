from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'isbn', 'category', 
        'availability', 'publication_date', 'created_at'
    ]
    list_filter = ['category', 'availability', 'language', 'created_at']
    search_fields = ['title', 'author', 'isbn', 'publisher']
    list_editable = ['availability']
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informacioni Bazë', {
            'fields': ('title', 'author', 'isbn', 'description')
        }),
        ('Detajet e Publikimit', {
            'fields': ('publisher', 'publication_date', 'pages', 'language')
        }),
        ('Kategorizimi', {
            'fields': ('category', 'availability')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['created_at', 'updated_at']
        return self.readonly_fields