from django.contrib import admin

from galleryapp.models import Gallery

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Gallery,GalleryAdmin)
