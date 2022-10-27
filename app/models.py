from calendar import calendar
from django.db import models



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
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'calendar_event'

