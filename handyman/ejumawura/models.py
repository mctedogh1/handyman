from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contact = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='images/')
    user_type = models.IntegerField(default=2)

    def __str__(self):
        return self.user.username
        
class Community(models.Model):
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name+ " - " + self.community.name



class Sex(models.Model):
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.sex

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    house_number = models.CharField(max_length=10)
    banner = models.ImageField(blank=True, null=True, upload_to='images/')
    status = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=10)
    gh_card = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.author} - {self.category}"