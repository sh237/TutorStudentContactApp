from django.urls import path
from .views import AccountRegistration,Logout,Login,Welcome

app_name = 'accounts'
urlpatterns = [
    path('register', AccountRegistration.as_view(), name="register"),
    path("logout",Logout,name="logout"),
    path('login', Login,name='login'),
    path('', Welcome.as_view(),name='welcome'),
]



