from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Groups, People, Subjects


class Search(View):

    def get(self, request):
        query = request.GET.get('q', '')

        if not query:
            return redirect("home")

        terms: list[str] = query.split()

        people_l = []
        groups_l = []
        subjects_l = []

        for t in terms:
            t = t.lower()
            groups = Groups.objects.filter(name__icontains=t)
            subjects = Subjects.objects.filter(name__icontains=t)
            people = People.objects.filter(Q(first_name__icontains=t)
                                           | Q(last_name__icontains=t)
                                           | Q(father_name__icontains=t))
            people_l += people
            groups_l += groups
            subjects_l += subjects

        return render(request, "users/search/search_results.html",
                      {'groups': groups_l, 'people': people_l, 'subjects': subjects_l, 'q': query})
