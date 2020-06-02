from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Subjects, Marks
from mainapp.util import is_decan


class Subject(View):

    def get(self, request, id):
        s = Subjects.objects.get(id=id)

        tid = request.session.get('tid')

        return render(request, 'users/subjects/subject.html', {'subject': s,
                                                               'tid': tid,
                                                               'decan': is_decan(request)})

    def post(self, request, id):
        s = Subjects.objects.get(id=id)

        marks = Marks.objects.filter(subject__id=id)
        marks.delete()

        s.delete()

        return redirect('home')


class SubjectAll(View):

    def get(self, request):
        s = Subjects.objects.all()

        return render(request, 'users/subjects/subjects.html', {'subjects': s,
                                                                'is_subjects': True,
                                                                'decan': is_decan(request)})

    def post(self, request):
        name = request.POST.get('name', '')

        if name:
            Subjects.objects.create(name=name)

        return redirect('subjects')
