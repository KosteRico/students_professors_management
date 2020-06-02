"""db_client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainapp.views import login, register, home, search, group, man, mark, subject, stats

urlpatterns = [
    path('api/stats', stats.get_stats_data, name='getStatsData'),
    path('groups/<int:id>', group.Group.as_view(), name='group'),
    path('stats/', stats.Stats.as_view(), name='stats'),
    path('subjects/<int:id>', subject.Subject.as_view(), name='subject'),
    path('people/<int:id>', man.Man.as_view(), name='people'),
    path('marks/<int:id>', mark.Mark.as_view(), name='mark'),
    path('marks/new/', mark.NewMark.as_view(), name='newMark'),
    path('', home.HomePage.as_view(), name='home'),
    path('admin', admin.site.urls),
    path('login', login.Login.as_view(), name='login'),
    path('register', register.Register.as_view(), name='register'),
    path('search', search.Search.as_view(), name='search'),
    path('groups/', group.GroupAll.as_view(), name='groups'),
    path('subjects/', subject.SubjectAll.as_view(), name='subjects'),
    path('people/', man.ManAll.as_view(), name='peopleAll'),
]
