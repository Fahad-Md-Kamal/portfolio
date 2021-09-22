from django.contrib import admin

from . import models



@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'efficiency')
    list_filter = ('category', 'efficiency')
    list_editable = ('efficiency',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Technology)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial')
    list_editable = ('serial',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.AboutMe)
admin.site.register(models.Education)
admin.site.register(models.Platform)
admin.site.register(models.Project)
