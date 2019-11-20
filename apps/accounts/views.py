from django.contrib.auth import login, logout as auth_logout

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .forms import LoginForm


class Login(View):
    def get(self, request):
        login_form = LoginForm()
        next_url = request.GET.get('next', None)
        return render(request, 'accounts/login.html', {
            'login_form': login_form,
            'next_url': next_url
        })

    def post(self, request):
        login_form = LoginForm(data=request.POST)
        next_url = request.GET.get('next', None)
        if login_form.is_valid():
            login(self.request, login_form.get_user())
            return redirect(next_url) if next_url else redirect('/')
        return render(request, 'accounts/login.html', {
            'login_form': login_form,
            'next_url': next_url
        })


class Logout(View):
    def get(self, request):
        next_url = request.GET.get('next', None)
        auth_logout(request)
        next_path = '?next={}'.format(next_url.replace("'", ""))
        return redirect('{}{}'.format(reverse('login'), next_path))
