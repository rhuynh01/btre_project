from django.urls import path
from listings import views

urlpatterns = [
    path('', views.IndexView, name='listings'),                     # url = listings/
    path('<int:listing_id>', views.ListingView, name='listing'),    # url = listings/id
    path('search/', views.SearchView, name='search'),                # url = listings/search

]
