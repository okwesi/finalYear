from django.contrib import admin
from . models import Blog, Comment
# Register your models here.

admin.site.register(Blog)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name',  'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

