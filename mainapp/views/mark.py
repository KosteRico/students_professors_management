from datetime import datetime
from django.utils.dateparse import parse_date

from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Marks, People, Subjects


class Mark(View):

    def get(self, request, id):
        mark = Marks.objects.get(id=id)

        return render(request, "users/mark/mark.html", {'mark': mark})

    def post(self, request, id):
        a = request.POST['action']

        m = Marks.objects.get(id=id)

        if a == 'delete':
            m.delete()
            return redirect('people', m.student.id)
        elif a == 'save':
            val = request.POST.get('mark', '')
            if val:
                m.value = val
                m.save()
            return redirect('mark', id)


class NewMark(View):

    def post(self, request):
        act = request.POST['action']

        if act == 'clear':
            return redirect('newMark')

        t = request.POST['teacher']
        s = request.POST['student']
        m = request.POST['mark']
        d = request.POST['date']
        sub = request.POST['subject']

        mark = Marks()
        mark.value = m
        mark.subject = Subjects.objects.get(id=sub)
        mark.teacher = People.objects.get(id=t)
        mark.student = People.objects.get(id=s)
        mark.time_created = parse_date(d)
        mark.save()

        return redirect('people', s)

    def get(self, request):
        t = request.GET.get('t', '')
        s = request.GET.get('s', '')
        group = request.GET.get('g', '')
        sub = request.GET.get('sub', '')

        ctx = {}

        t_sess = request.session.get('tid', '')

        if t_sess:
            ctx['t_selected'] = People.objects.get(id=t_sess)
        if t:
            ctx['t_selected'] = People.objects.get(id=t)
        else:
            ctx['teachers'] = People.objects.filter(type='T')

        if s:
            ctx['s_selected'] = People.objects.get(id=s)
        elif group:
            ctx['students'] = People.objects.filter(type='S', group__id=group)
        else:
            ctx['students'] = People.objects.filter(type='S')

        if sub:
            ctx['sub_selected'] = Subjects.objects.get(id=sub)
        else:
            ctx['subjects'] = Subjects.objects.all()

        return render(request, 'users/mark/new_mark.html', ctx)
