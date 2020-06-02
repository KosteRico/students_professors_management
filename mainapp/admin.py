from django.contrib import admin

# Register your models here.
from mainapp.models import Groups, People, Marks, Subjects


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    exclude = ('id',)


@admin.register(Marks)
class MarkAdmin(admin.ModelAdmin):
    exclude = ('id',)


@admin.register(Subjects)
class SubjectAdmin(admin.ModelAdmin):
    exclude = ('id',)


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    exclude = ('id',)
