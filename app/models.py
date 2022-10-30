from calendar import calendar
from django.db import models
from accounts.models import User


class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
    tutor = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='tutor')
    student = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tutor.username + " " + self.student.username

    class Meta:
        db_table = 'calendar'

class Month(models.Model):
    id = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='calendar')
    month = models.DateField()
    target = models.CharField(max_length=128)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'month'




class CalendarEvent(models.Model):
    id = models.AutoField(primary_key=True)
    calendar = models.ForeignKey('Calendar', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=40, default='rgb(24,118,210)')
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'calendar_event'

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application_student')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application_tutor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.username + " " + self.tutor.username

    class Meta:
        db_table = 'application'