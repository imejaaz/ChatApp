from django.urls import path
from . import views



urlpatterns = [
    path('post-list/', views.post_views, name='post-list'),
    path('open/<int:id>/', views.post_open_view, name='open'),
]