from tkinter import E
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Calendar, Month, CalendarEvent, Application
from accounts.models import User
import json
from datetime import date, datetime

# def index(request):
#     template = loader.get_template("app/index.html")
#     context = {}
#     return HttpResponse(template.render(context,request))

# # Create your views here.
# @login_required



class TutorHomeView(TemplateView,LoginRequiredMixin):
    template_name = "app/tutor_home.html"
    # template_name = "app/student_list.html"
    def get_context_data(self, **kwargs):
        calendar = Calendar.objects.filter(tutor=self.request.user.id )
        application = Application.objects.filter(tutor=self.request.user.id )
        context = super().get_context_data(**kwargs)
        context["student_list"] = [[v.student.username, v.student.last_name, v.student.first_name, v.student.id ] for v in calendar]
        context["application_list"] = [[v.student.username, v.student.last_name, v.student.first_name, v.student.id] for v in application]
        context["user"] = self.request.user
        return context

class StudentHomeView(TemplateView,LoginRequiredMixin):
    template_name = "app/student_home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))

class StudentCalendarView(TemplateView,LoginRequiredMixin):
    template_name = "app/calendar.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        student = User.objects.get(id=self.request.user.id)
        tutor = User.objects.get(id=kwargs["tutor_id"])
        event = CalendarEvent.objects.filter(calendar__student=student, calendar__tutor=tutor)
        context["calendar_id"] = Calendar.objects.get(student=student, tutor=tutor).id
        context["tutor"] = tutor
        context["event_list"] = json.dumps([{"start":v.start,"end": v.end,"title": v.title, "id":v.id,"color":v.color} for v in event],default=json_serial)
        user = self.request.user
        if user.is_teacher:
            context["is_display"] = True
        else:
            if Calendar.objects.filter(student=user).exists():
                context["is_display"] = True
            else:
                context["is_display"] = False
        return context
        return context

class TutorCalendarView(TemplateView,LoginRequiredMixin):
    template_name = "app/calendar.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        tutor = User.objects.get(id=self.request.user.id)
        student = User.objects.get(id=kwargs["student_id"])
        event = CalendarEvent.objects.filter(calendar__student=student, calendar__tutor=tutor)
        context["calendar_id"] = Calendar.objects.get(student=student, tutor=tutor).id
        context["student"] = student
        context["event_list"] = json.dumps([{"start":v.start,"end": v.end,"title": v.title, "id":v.id, "color":v.color} for v in event],default=json_serial)
        context["is_teacher"] = True
        return context

class SettingView(TemplateView,LoginRequiredMixin):
    template_name = "app/setting.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        if user.is_teacher:
            context["is_display"] = True
        else:
            if Calendar.objects.filter(student=user).exists():
                tutor = Calendar.objects.filter(student=user)[0].tutor
                context["tutor"] = tutor
                context["is_display"] = True
            else:
                context["is_display"] = False
        return context

# class CalendarView(TemplateView,LoginRequiredMixin):
#     template_name = "app/calendar.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["user"] = self.request.user
#         return context

def userDelete(request):
    id = request.POST.get('user_id')
    if(user != None):
        user = User.objects.get(id=id).delete()
        return JsonResponse({'result':'success'})
    else:
        return JsonResponse({'result':'failed'})


def searchTutor(request):
    id = request.POST.get('id')
    tutor = User.objects.get(id=id)
    if(tutor != None and tutor.is_teacher):
        return JsonResponse({'tutor_name':tutor.username,'tutor_id':tutor.id})
    else:
        return JsonResponse({'tutor':None, 'tutor_id':None})

def getRequested(request):
    application = None
    if Application.objects.filter(student=request.user.id).exists():
        application = Application.objects.filter(student=request.user.id)[0]
    
    if(application != None):
        return JsonResponse({'tutor_name':application.tutor.username,'tutor_id':application.tutor.id})
    else:
        return JsonResponse({'tutor':None, 'tutor_id':None})

def application(request,tutor_id):
    tutor = User.objects.get(id=tutor_id)
    if  Application.objects.filter(tutor=tutor,student=request.user).exists():
        Application.objects.filter(student=request.user.id).delete()
    Application.objects.create(tutor=tutor,student=request.user)
    return JsonResponse({'tutor_name':tutor.username,'tutor_id':tutor.id})

def approve(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student = User.objects.get(id=student_id)
        if Application.objects.filter(student=student, tutor=request.user).exists():
            Application.objects.filter(student=student, tutor=request.user).delete()
            Calendar.objects.create(tutor=request.user,student=student)
            return JsonResponse({'result':'success'})
    return JsonResponse({'result':'failed'})

def rejection(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student = User.objects.get(id=student_id)
        if Application.objects.filter(student=student, tutor=request.user).exists():
            Application.objects.filter(student=student, tutor=request.user).delete()
            return JsonResponse({'result':'success'})
    return JsonResponse({'result':'failed'})

def eventUpdate(request):
    if request.method == "POST":
        event_id = request.POST.get('event_id')
        title = request.POST.get('title')
        start = request.POST.get('start')
        end = request.POST.get('end')
        print(event_id)
        print(start)
        print(end)
        event = CalendarEvent.objects.get(id=event_id)
        event.start = datetime.strptime(start,"%Y-%m-%d %H:%M:%S") 
        event.end = datetime.strptime(end,"%Y-%m-%d %H:%M:%S") 
        event.title = title
        event.save()
        # if Application.objects.filter(student=student, tutor=request.user).exists():
        #     Application.objects.filter(student=student, tutor=request.user).delete()
        #     return JsonResponse({'result':'success'})
        
        return JsonResponse({'result':'success'})
    return JsonResponse({'result':'failed'})

def eventDelete(request):
    if request.method == "POST":
        event_id = request.POST.get('event_id')
        print(event_id)
        event = CalendarEvent.objects.get(id=event_id)
        event.delete()
        return JsonResponse({'result':'success'})
    return JsonResponse({'result':'failed'})

def eventCreate(request):
    if request.method == "POST":
        calendar_id = request.POST.get('calendar_id')
        title = request.POST.get('title')
        start = request.POST.get('start')
        end = request.POST.get('end')
        color = request.POST.get('color')
        calendar = Calendar.objects.get(id=calendar_id)
        event = CalendarEvent.objects.create(calendar = calendar, title=title,start = datetime.strptime(start,"%Y-%m-%d %H:%M:%S"),end = datetime.strptime(end,"%Y-%m-%d %H:%M:%S"),color=color)
        return JsonResponse({'result':'success','event_id':event.id})
    return JsonResponse({'result':'failed'})




#例
def ajax_number(request):
    number1 = int(request.POST.get('number1'))
    number2 = int(request.POST.get('number2'))
    plus = number1 + number2
    minus = number1 - number2
    d = {
        'plus': plus,
        'minus': minus,
    }
    return JsonResponse(d)