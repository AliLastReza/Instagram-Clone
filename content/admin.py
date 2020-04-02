from django.contrib import admin
from django.contrib.admin import register


# Register your models here.
from content.models import Post, PostMedia, Tag, PostTag, TagegedUser


class PostMediaInline(admin.TabularInline):
    model = PostMedia


class PostTagInline(admin.TabularInline):
    model = PostTag


class TaggedUserInline(admin.TabularInline):
    model = TagegedUser


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('caption', 'user', 'location')
    inlines = (PostMediaInline, PostTagInline, TaggedUserInline)


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time')