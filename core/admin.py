from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# from .models import User, User_Post


# Register your models here.
admin.site.register(User, UserAdmin)

# @admin.register(User_Post)
# class User_PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user')
#     exclude = ('slug',)
