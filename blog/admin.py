from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('id', 'name',
                    'created_at', 'slug')
    list_display_links = ('name', )
    list_editable = ('slug', )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('id', 'name',
                    'created_at', 'slug')
    list_display_links = ('name', )
    list_editable = ('slug', )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'title', 'category',
                    'created_at', 'views')
    list_display_links = ('title', )
