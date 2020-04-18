from django.conf.urls import url
from django.urls import include, path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index , name="index" ),
    path('courses' , courses , name="courses"),
    path('course/<slug>', course_detail , name="course-detail"),
    path('login' , login ,name="login"),
    path('register' , register ,name="register"),
    path('sucess',mail , name="success"),
    path('verification/<slug>', verification , name="verification"),
    
  
]
