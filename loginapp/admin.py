from django.contrib import admin
from .models import User, Video


class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']


class VideoAdmin(admin.ModelAdmin):
    search_fields = ['object']


# Register your models here.
admin.site.register(User, UserAdmin)  # admin에 User 검색 기능 추가
admin.site.register(Video, VideoAdmin)  # admin에 User 검색 기능 추가