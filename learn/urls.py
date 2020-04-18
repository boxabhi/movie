from django.conf.urls import url
from django.urls import include, path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index , name="index" ),
    path('courses' , courses , name="courses"),
    path('course/<slug>', course_detail , name="course-detail"),
    path('login' , login ,name="login"),
    path('register' , register ,name="register"),
    path('sucess',mail , name="success"),
    path('verification/<slug>', verification , name="verification"),
    
  
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()