from __future__ import unicode_literals
from django.db import models
import datetime
from chzis.congregation.models import CongregationMember


class Lesson(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    reading = models.BooleanField(default=False)
    demo = models.BooleanField(default=False)
    discourse = models.BooleanField(default=False)
    book_page = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    last_modification = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return "{number} {name}".format(number=self.number, name=self.name)

    class Meta:
        ordering = ['number']


class Background(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    last_modification = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return "{number} {name}".format(number=self.number, name=self.name)

    class Meta:
        ordering = ['number']


class SchoolTask(models.Model):
    topic = models.CharField(max_length=255)
    person = models.ForeignKey(CongregationMember)
    lesson = models.ForeignKey(Lesson)
    background = models.ForeignKey(Background, null=True, blank=True)
    presentation_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateField(auto_now=True)
    last_modification = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return "{number} {lastname} {firstname} {topic}".format(number=self.id,
                                                                lastname=self.person.user.last_name,
                                                                firstname=self.person.user.first_name,
                                                                topic=self.topic)

    def get_absolute_url(self):
        return "/school/tasks/{id}".format(id=self.id)

    class Meta:
        permissions = (
                    ("can_view_all_tasks", "Can see all available tasks"),
                    ("can_judge_tasks", "Can judge presented tasks by popele"),
                )

class SchoolMemberTasksResults(models.Model):
    person = models.ForeignKey(CongregationMember)
    lesson = models.ForeignKey(Lesson)
    task = models.ForeignKey(SchoolTask, null=True, blank=True, default=None)
    lesson_passed = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    lesson_passed_date = models.DateTimeField(auto_now=True, null=True)
    last_modification = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return "{lesson} {lastname} {firstname} {passed}".format(lesson=self.lesson.name,
                                                                 lastname=self.person.user.last_name,
                                                                 firstname=self.person.user.first_name,
                                                                 passed=self.lesson_passed)