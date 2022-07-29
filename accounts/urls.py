# Copyright (c) 2022 Nima Ghasemi Por
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



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