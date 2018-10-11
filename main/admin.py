from django.contrib import admin
from .models import UserInfo, Project, Skill, Education, Work

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Work)