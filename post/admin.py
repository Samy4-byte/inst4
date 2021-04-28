from django.contrib import admin

from .models import Post, PostImage
# Register your models here.

class PostImagesInline(admin.TabularInline):
    model = PostImage
    image = ['image', ]

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImagesInline, ]

    list_display = ['id', 'title']


admin.site.register(Post, PostAdmin)