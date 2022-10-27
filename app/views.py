from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# def index(request):
#     template = loader.get_template("app/index.html")
#     context = {}
#     return HttpResponse(template.render(context,request))

# # Create your views here.
# @login_required



class TutorHomeView(TemplateView,LoginRequiredMixin):
    template_name = "app/calendar.html"
    # template_name = "app/student_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

class StudentHomeView(TemplateView,LoginRequiredMixin):
    template_name = "app/calendar.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

# class CalendarView(TemplateView,LoginRequiredMixin):
#     template_name = "app/calendar.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["user"] = self.request.user
#         return context


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