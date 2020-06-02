from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View


class Login(View):

    def get(self, request):
        logout(request)
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        u: User = authenticate(username=username, password=password)

        if u is not None:
            login(request, u)
            try:
                um = u.man
                request.session['tid'] = u.man.id
            except ObjectDoesNotExist:
                pass
            return redirect("home")

        return
