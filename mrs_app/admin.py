from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Movie, Rating

# Register your models here.


admin.site.register(Movie)
admin.site.register(Rating)