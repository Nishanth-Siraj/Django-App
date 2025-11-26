from django.contrib import admin
from .models import Post, Tags


class PostAdminTable(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at')

class TagsAdmin(admin.ModelAdmin):
    listdisplay = ['post','tag']

admin.site.register(Post, PostAdminTable)
admin.site.register(Tags, TagsAdmin)
