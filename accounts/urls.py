# Neveshtar
# Copyright (C) 2022  radiumatic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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