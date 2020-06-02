from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import People, Groups


class Register(View):

    def get(self, request):

        r = request.GET.get('role')

        return render(request, "auth/register.html")

    def post(self, request):

        if 'next' in request.POST:
            r = request.POST['role']
            ctx = {"role": r}
            if r == 'pro':
                current_groups = Groups.objects.all()
                ctx['groups'] = current_groups
            return render(request, "auth/register.html", ctx)

        username = request.POST['username']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        father_name = request.POST.get('fatherName')
        group_num = request.POST.get('groupId')
        password = request.POST['password']
        password_confirm = request.POST['passwordConfirm']

        if password != password_confirm:
            return render(request, "auth/register.html", {'error_msg': "Разные пароли!"})

        user = User.objects.create_user(username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        if father_name and group_num:
            prof = People.objects.create()

            prof.first_name = first_name
            prof.last_name = last_name
            prof.father_name = father_name
            prof.type = 'T'
            prof.group = Groups.objects.get(id=group_num)

            prof.u = user
            prof.save()

        return redirect('home')
