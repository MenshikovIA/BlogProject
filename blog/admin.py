from django.contrib import admin
from django.contrib.auth.models import User
from blog.models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):

    pass
