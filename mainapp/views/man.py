from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from mainapp.models import People, Marks, Groups
from mainapp.util import is_decan


class Man(View):

    def get(self, request, id):
        man = People.objects.get(id=id)

        ctx = {'man': man}

        tid = request.session.get('tid', '')
        if tid:
            ctx['tid'] = tid
        elif request.user.is_authenticated:
            ctx['decan'] = True

        return render(request, "users/people/man.html", ctx)

    def post(self, request, id):
        man = People.objects.get(id=id)

        marks = None

        if man.is_student():
            marks = Marks.objects.filter(student__id=man.id)
        elif man.is_teacher():
            marks = Marks.objects.filter(teacher__id=man.id)
            man.u.delete()

        marks.delete()

        man.delete()

        return redirect('home')


class ManAll(View):

    def get(self, request):

        type = request.GET.get('type', '')

        ctx = {'is_people': True, 'decan': is_decan(request)}

        if type:
            p = People.objects.filter(type=type)
            ctx['people'] = p
            ctx['type'] = type
        else:
            return redirect(reverse('peopleAll') + '?type=S')

        if ctx['decan']:
            g = Groups.objects.all()
            ctx['groups'] = g

        return render(request, 'users/people/people.html', ctx)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        type = 'S'
        group = request.POST.get('group')

        if not(first_name or last_name or type or group):
            return redirect(reverse('peopleAll') + '?type=' + type)

        man = People()
        man.type = type
        man.group = Groups.objects.get(id=group)
        man.father_name = father_name
        man.first_name = first_name
        man.last_name = last_name
        man.save()

        return redirect(reverse('peopleAll') + '?type=' + type)
