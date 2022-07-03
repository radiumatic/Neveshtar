from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/' , views.login, name='login'),
    path('logout/' , LogoutView.as_view(), name='logout'),
    path('register/' , views.register, name='register'),
    path('reset_password/' , views.reset_password, name='reset_password'),
    path('account_activation_sent/' , views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/' , views.activate, name='activate'),
    path('reset_password_sent/' , views.reset_password_sent, name='reset_password_sent'),
    path('reset_password_confirm/<uidb64>/<token>/' , views.reset_password_confirm, name='reset_password_confirm'),
    path('reset_password_done/' , views.reset_password_done, name='reset_password_done'),
    

]