from django.contrib import admin
from listings.models import Listing

# Code to customize the display in the Admin model listing
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor', 'is_published', 'price', 'list_date')
  # list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)
# admin.site.register(Listing)
