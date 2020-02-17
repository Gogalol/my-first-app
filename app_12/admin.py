from django.contrib import admin
from .models import Post
admin.site.regisre(Post)
py manage.py restart server