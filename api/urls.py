from django.urls import path
from . import views
urlpatterns=[
    path('add_like/<int:pk>/', views.add_like, name='add_like'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('remove_like/<int:pk>/', views.remove_like, name='remove_like'),

]
