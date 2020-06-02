from django.shortcuts import render
from django.views import View


class HomePage(View):

    def get(self, request):
        print()
        return render(request, "users/home.html", {'is_home': True})
