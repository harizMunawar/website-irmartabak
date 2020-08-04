from django.contrib import admin
from .models import martabak
from imagekit.admin import AdminThumbnail
import admin_thumbnails

@admin.register(martabak)
@admin_thumbnails.thumbnail('image')
class MartabakAdmin(admin.ModelAdmin):
    martabak_thumbnail = AdminThumbnail(image_field='preview', template='thumbnail.html')
    list_display = ('name', 'variant', 'lowest_price', 'highest_price', 'deskripsi', 'image_thumbnail')
    search_fields = ('name', 'variant', 'lowest_price', 'highest_price')
    readonly_fields = ('slug', 'martabak_thumbnail')
    fields = ('id', 'name', 'lowest_price', 'highest_price', 'variant', 'deskripsi', 'best_seller', 'image', 'martabak_thumbnail', 'size_besar', 'size_kecil')
