from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('account/', views.signup, name='account'),
]
