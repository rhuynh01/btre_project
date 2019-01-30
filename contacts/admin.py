from django.contrib import admin
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  list_filter = ('name', 'email', 'listing')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25

# Register your models here.
admin.site.register(Contact, ContactAdmin)
