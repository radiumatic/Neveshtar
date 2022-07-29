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



from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.shortcuts import render
from .forms import RegisterForm, ResetPasswordForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from .tokens import EmailTokenGenerator
from django.core.mail import send_mail
from os import getenv
from django.contrib.auth import get_user_model
User = get_user_model()
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                render (request, 'accounts/register.html', {'error': 'ایمیل وارد شده تکراری است'})
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'لطفا ایمیل خود را تایید کنید'
            uid = urlsafe_b64encode(force_bytes(user.pk))
            print(uid)
            message = render_to_string('accounts/account_activation_email.html', {
                'fullname': user.first_name + ' ' + user.last_name,
                'domain': current_site.domain,
                'uid': uid.decode(),
                'token': EmailTokenGenerator().make_token(user),
            })
            to = form.cleaned_data['email']
            send_mail(subject, message, getenv('EMAIL_HOST_USER'), [to])
            return HttpResponseRedirect('/accounts/account_activation_sent/')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html')
def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')
def activate(request, uidb64, token):
    try:
        print(uidb64)
        uid = force_bytes(urlsafe_b64decode(uidb64))
        print(uid.decode())
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and EmailTokenGenerator().check_token(user, token):
        user.is_active = True
        user.save()
        login_user(request, user)
        status = 'اکانت شما فعال شد'
        return render(request, 'accounts/account_activation_sent.html', {'status': status})
    else:
        status = 'لینک فعال سازی اکانت شما نامعتبر است'
        return render(request, 'accounts/account_activation_sent.html', {'status': status})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است'})
    else:
        return render(request, 'accounts/login.html')
def reset_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(email=username)
        current_site = get_current_site(request)
        subject = 'درخواست تغییر رمز عبور'
        message = render_to_string('accounts/reset_password_email.html', {
            'fullname': user.first_name + ' ' + user.last_name,
            'domain': current_site.domain,
            'uid': urlsafe_b64encode(force_bytes(user.pk)).decode(),
            'token': EmailTokenGenerator().make_token(user),
        })
        to = user.email
        send_mail(subject, message, getenv('EMAIL_HOST_USER'), [to])
        return HttpResponseRedirect('/accounts/reset_password_sent/')
    else:
        return render(request, 'accounts/reset_password.html')
def reset_password_sent(request):
    return render(request, 'accounts/reset_password_sent.html')
def reset_password_confirm(request, uidb64, token):
    if not request.method == "POST":
        try:
            uid = force_bytes(urlsafe_b64decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and EmailTokenGenerator().check_token(user, token):
            return render(request, 'accounts/reset_password_confirm.html',{'uidb64':uidb64,'token':token})
        else:
            return render(request, 'accounts/reset_password_sent.html', {'status': 'لینک تغییر پسورد نامعتبر است'})
    else:
        user = User()
        try:
            uid = force_bytes(urlsafe_b64decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and EmailTokenGenerator().check_token(user, token):
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user.set_password(request.POST['password1'])
                user.save()
                return HttpResponseRedirect('/accounts/reset_password_done/')
            else:
                return render(request, 'accounts/reset_password_confirm.html', {"error":"پسورد شما اعتبار لازم را ندارد",'uidb64':uidb64,'token':token}) 
        else:
            return render(request, 'accounts/reset_password_sent.html', {'status': 'لینک تغییر پسورد نامعتبر است'})
def reset_password_done(request):
    return render(request, 'accounts/reset_password_done.html')





                

            




  