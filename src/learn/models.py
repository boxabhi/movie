from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,password,v_token,verify,mobile,address):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        v_token = self.v_token
        verify = self.verify
        mobile = self.mobile
        address = self.address
        user = self.model(email=email, v_token =v_token, verify=verify, mobile=mobile, address=address)
        user.set_password(password)
        user.save(using =self.db)
        
        return user
    
    def create_superuser(self, email, password,v_token,verify,mobile,address ,**extra_fields):
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.v_token = v_token
        user.mobile = mobile
        user.address = address
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        
        user.save(using =self.db)
        return user


class Profile(AbstractUser):
    username = None
    email = models.CharField(unique=True, max_length=200)
    v_token = models.CharField(max_length=5000)
    verify = models.BooleanField(default=False)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=4000 ,blank=True)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'v_token','address','verify','mobile']
    objects = CustomUserManager()

    def __str__(self):
        return self.email



    
    
  
    


class Course(models.Model):
    course_name = models.CharField(max_length=1000)
    details = models.CharField(max_length=5000)
    image = models.ImageField(upload_to = "courses/" )
    slug = models.CharField(max_length=400,unique=True,default='')
    syllabus = models.CharField(max_length=500)
    prerequisites = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.course_name
    
  
class Module(models.Model):
    topic = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.topic
    