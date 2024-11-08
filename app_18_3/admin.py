from django.contrib import admin

# Register your models here.
# app_18_3/admin.py

from .models import Resume, Experience, Education, Skill

admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
