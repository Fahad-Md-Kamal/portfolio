from django.contrib import admin

from . import models


admin.site.register(models.AboutMe)
admin.site.register(models.Technology)
admin.site.register(models.TechFramework)
admin.site.register(models.Skill)
admin.site.register(models.Education)
admin.site.register(models.Platform)
admin.site.register(models.Project)
