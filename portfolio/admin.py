from django.contrib import admin

from . import models


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'efficiency')
    list_filter = ('category', 'efficiency')
    list_editable = ('efficiency', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial')
    list_editable = ('serial',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'platform', 'serial_num')
    list_editable = ('serial_num', 'platform')
    prepopulated_fields = {'slug': ('project_name',)}


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', )
    list_editable = ('designation',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact', 'serial')
    list_editable = ('serial',)

@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'serial')
    list_editable = ('serial',)

admin.site.register(models.OtherURLS)
admin.site.register(models.AboutMe)
admin.site.register(models.Education)
admin.site.register(models.Platform)
