import random

from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.dateparse import parse_date

from mainapp.models import Subjects, Groups, People, Marks


def get_avg(request):
    date_before = request.GET.get('date_before')
    date_after = request.GET.get('date_after')
    t = request.GET.get('teacher')
    g = request.GET.get('group')
    s = request.GET.get('subject')

    res = Marks.objects.all().values('student__id') \
        .annotate(avg=Avg('value')) \
        .values('student', 'avg')

    if date_before:
        if date_after:
            res = res.filter(time_created__range=[parse_date(date_before), parse_date(date_after)])
        else:
            res = res.filter(time_created__gte=parse_date(date_before))
    elif date_after:
        res = res.filter(time_created__lte=parse_date(date_after))

    if t:
        res = res.filter(teacher__id=t)
    if g:
        res = res.filter(student__group__id=g)
    if s:
        res = res.filter(subject__id=s)

    student_ids = [i[0] for i in res.values_list('student')]

    values = [i[0] for i in res.values_list('avg')]

    return student_ids, values


class Stats(View):

    def get(self, request):
        s = Subjects.objects.all()
        g = Groups.objects.all()
        teachers = People.objects.filter(type='T')

        a = request.GET.get('type')
        #
        ctx = {'is_stats': True, 'groups': g,
               'teachers': teachers,
               'subjects': s,
               'is_graph': a == 'graph',
               'is_table': a == 'table'}

        if ctx['is_table']:
            student_ids, values = get_avg(request)

            values = [round(i, 3) for i in values]

            students = []
            for id in student_ids:
                students.append(People.objects.get(id=id))

            stud_set = [(students[i], values[i]) for i in range(len(students))]

            stud_set.sort(key=lambda tup: -tup[1])

            ctx['students'] = stud_set

        return render(request, 'users/stats/stats.html', ctx)


def get_stats_data(request):
    student_ids, values = get_avg(request)

    names = []

    bg_colors = []
    border_colors = []

    for i in student_ids:
        names.append(People.objects.get(id=i).full_name())

    for i in range(len(names)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        bg_col = 'rgba(%s, %s, %s, .4)' % (r, g, b)
        border_col = 'rgba(%s, %s, %s, 1)' % (r, g, b)
        bg_colors.append(bg_col)
        border_colors.append(border_col)

    data = {
        'labels': names,
        'datasets': [{
            # 'label': 'График',
            'data': values,
            'backgroundColor': bg_colors,
            'borderColor': border_colors,
            'borderWidth': 1
        }],
    }

    return JsonResponse(data)
