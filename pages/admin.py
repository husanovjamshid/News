from django.contrib import admin
from .models import Category, RightNews, CenterNews, Contact

# Register your models here.

admin.site.register(RightNews)
admin.site.register(CenterNews)
admin.site.register(Category)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date', 'message')
admin.site.register(Contact, ContactAdmin)