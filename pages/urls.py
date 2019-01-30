from django.urls import path
from pages import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('about', views.about, name='about'),
    # path('about1', views.about1, name='about1'),
    path('', views.IndexView, name='index'),
    path('about/', views.AboutView, name='about'),
]
