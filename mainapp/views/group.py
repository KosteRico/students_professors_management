from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Groups, People
from mainapp.util import is_decan


class Group(View):

    def get(self, request, id):
        g = Groups.objects.get(id=id)

        ctx = {'group': g, 'decan': is_decan(request)}

        return render(request, "users/groups/group.html", ctx)

    def post(self, request, id):
        g = Groups.objects.get(id=id)

        people = People.objects.filter(group__id=id)
        people.delete()

        g.delete()

        return redirect('groups')


class GroupAll(View):

    def get(self, request):
        g = Groups.objects.all()

        return render(request, 'users/groups/groups.html',
                      {'groups': g, 'is_groups': True,
                       'decan': is_decan(request)})

    def post(self, request):
        name = request.POST.get('name', '')

        if name:
            g = Groups.objects.filter(name=name)
            if len(g) == 0:
                Groups.objects.create(name=name)

        return redirect('groups')
