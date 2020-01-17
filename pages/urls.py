from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('creativity', views.creativity, name="creativity"),
    path('critical_thinking', views.critical_thinking, name="critical_thinking"),
    path('career_management', views.career_management, name="career_management"),
    path('time_management', views.time_management, name="time_management"),
    path('professionalism', views.professionalism, name="professionalism"),
    path('reflection', views.reflection, name="reflection"),
]
