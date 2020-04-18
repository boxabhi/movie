from django.shortcuts import render,redirect
from .models import Profile, Course
import random, string
from django.core.mail import send_mail
# Create your views here.
from django.conf import settings

from django.contrib.auth import authenticate

def index(request):
    courses = Course.objects.all()
    return render(request , 'front/index.html',{'courses' : courses})



def courses(request):
    courses = Course.objects.all()
    return render(request , 'front/courses.html', {'courses' : courses})



def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    return render(request , 'front/course-detail.html', {'course' : course})

def login(request):
    if request.method == 'POST':
        user = authenticate(email= request.POST.get('email'), password= request.POST.get('password'))
        u = Profile.objects.get(email = request.POST.get('email'))
        print(u)
        if user:
            return render(request,'sucess.html')
        else:
            return render(request,'front/login.html' , {'message': 'Wrong Credentials'})        
    return render(request , 'front/login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        user = Profile(email = email,v_token=token,mobile=mobile)
        user.set_password(password)
        user.save()
        
        send_mail('Account Verification','Your account needs to be verify and your verification link is http://127.0.0.1:8000/verification/{}'.format(token)
                  ,settings.EMAIL_HOST_USER,[request.POST['email']] ,fail_silently=False,)

        return redirect(mail)
    return render(request , 'front/register.html')


def mail(request):
    return render(request , 'front/mail.html')



def verification(request,slug):
    user = Profile.objects.filter(v_token = slug).first()
    print(user)
    if(user):
        user.verify = True
        user.save()
        return render(request , 'front/verification.html',{'user' : user.email})
    else:
        return render(request , 'custom/404.html')
