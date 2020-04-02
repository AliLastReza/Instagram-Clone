from django.contrib import admin

# Register your models here.
from activity.models import Comment, Like

admin.site.register(Comment)
admin.site.register(Like)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'replay_to')
