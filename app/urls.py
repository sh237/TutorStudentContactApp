from django.urls import path
from .views import TutorHomeView,StudentHomeView,TutorCalendarView,StudentCalendarView, searchTutor,application,getRequested,approve,rejection,eventUpdate,eventDelete,eventCreate,SettingView,userDelete

app_name = 'app'
urlpatterns = [
    path("tutor_home", TutorHomeView.as_view(), name="tutor_home"),
    path("tutor_calendar/<str:student_id>", TutorCalendarView.as_view(), name="tutor_calendar"),
    path("student_home", StudentHomeView.as_view(), name="student_home"),
    path("student_calendar/<str:tutor_id>/", StudentCalendarView.as_view(), name="student_calendar"),
    path("application/<str:tutor_id>", application, name="application"),
    path("ajax_search_tutor", searchTutor, name="ajax_search_tutor"),
    path("ajax_get_requested", getRequested, name="ajax_get_requested"),
    path("approve", approve, name="approve"),
    path("rejection", rejection, name="rejection"),
    path("ajax_event_update", eventUpdate, name="ajax_event_update"),
    path("ajax_event_delete", eventDelete, name="ajax_event_delete"),
    path("ajax_event_create", eventCreate, name="ajax_event_create"),
    path("setting", SettingView.as_view(), name="setting"),
    path("ajax_user_delete", userDelete, name="ajax_user_delete"),
]



