from django.urls import path
from .views import TutorHomeView,StudentHomeView

app_name = 'app'
urlpatterns = [
    path("tutor_home", TutorHomeView.as_view(), name="tutor_home"),
    path("student_home", StudentHomeView.as_view(), name="student_home"),
]



