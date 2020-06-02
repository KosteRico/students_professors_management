# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.name


class Marks(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey('People', models.DO_NOTHING, related_name='marks')
    teacher = models.ForeignKey('People', models.DO_NOTHING, related_name='+')
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, related_name='marks')
    value = models.FloatField()
    time_created = models.DateTimeField(default=timezone.now)

    def get_date(self):
        m = self.time_created.month
        d = self.time_created.day
        m_s = m
        d_s = d
        if 1 <= m <= 9:
            m_s = '0' + str(m)
        if 1 <= d <= 9:
            d_s = '0' + str(d)

        return '%s.%s.%s' % (d_s, m_s, self.time_created.year)

    class Meta:
        db_table = 'marks'

    def __str__(self):
        return "%s. Mark: %s. Subject: %s. Teacher: %s" % (self.student, self.value, self.subject, self.teacher)


class People(models.Model):
    id = models.IntegerField(primary_key=True)
    u = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='man', null=True, blank=True, default=None)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    def is_teacher(self):
        return self.type == 'T'

    def is_student(self):
        return self.type == 'S'

    class Meta:
        db_table = 'people'

    def full_name(self):
        return "%s %s %s" % (self.last_name.capitalize(), self.first_name.capitalize(), self.father_name.capitalize())

    def __str__(self):
        return "%s %s %s (type: %s)" % (self.last_name, self.first_name, self.father_name, self.type)


class Subjects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return self.name
