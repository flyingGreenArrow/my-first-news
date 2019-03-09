from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
    
    
class User_sys(models.Model):
    username = models.TextField(User)
    password = models.TextField()
    e_mail = models.EmailField()
    
    
    def create(self):
        self.user = User.objects.create_user(self.username, self.e_mail, self.password)
        self.user.save()
        
    def change_password(self):  # (self, passw)
        self.user = User.objects.get(username=self.username)  # some question
        self.user.set_password()  # (passw)
        self.user.save()
    
    def authenticate_that_user(self):
        user = authenticate()
        if user is not None:
            if username.is_active:
                print('User is valid, active and authenticate')
            else: 
                print("The password is valid, but the account has been disabled!")
        else:
            print("The username and password were incorrect.")
    
