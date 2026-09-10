from django.contrib import admin

from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'created_at')
    search_fields = ('name', 'email', 'service', 'message')
    list_filter = ('service', 'created_at')
