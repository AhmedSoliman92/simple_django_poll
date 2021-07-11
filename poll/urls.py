from django.urls import path
from poll import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('results/<id>/', views.results, name='results'),
    path('vote/<id>/', views.vote, name='vote'),

]
