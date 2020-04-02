from django.contrib import admin
# Register your models here.
from django.contrib.admin import register
from relation.models import Relation


@register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')