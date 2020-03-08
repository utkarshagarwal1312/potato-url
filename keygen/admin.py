from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from keygen.models import Key


@register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('val', 'is_used',)
