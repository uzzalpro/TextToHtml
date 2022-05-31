from django.contrib import admin
# from requests import post

# Register your models here.
from .models import Post

admin.site.register(Post)