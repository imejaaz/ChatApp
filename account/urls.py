from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile'),

]
