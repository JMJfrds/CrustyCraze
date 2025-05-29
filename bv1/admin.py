from django.contrib import admin
from bv1.models import ContactModel, SignUP


admin.site.register(SignUP)

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']
