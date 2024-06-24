import django
from django.contrib import admin
from ejumawura.models import UserProfile, Category, Post, Sex, Community

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Sex)
admin.site.register(Post)
admin.site.register(Community)
