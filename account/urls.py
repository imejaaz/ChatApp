from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('account/', views.signup, name='account'),

]
