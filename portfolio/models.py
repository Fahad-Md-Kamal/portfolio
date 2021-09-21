from django.db import models
from django.contrib.auth.models import User


class AboutMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.user.username



class Technology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.title

class TechFramework(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='tech_framework')
    name = models.CharField(max_length=255)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']
        verbose_name = 'TechFramework'
        verbose_name_plural = 'TechFrameworks'

    def __str__(self):
        return self.technology.title


SKILL_CATEGORIES = [
        (1, 'HARD'),
        (2, 'SOFT'),
    ]


class Skill(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=SKILL_CATEGORIES, default=1)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=100)
    organization = models.CharField(max_length=50)
    passing_year = models.IntegerField()
    achievement = models.CharField(max_length=10)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-passing_year']

    def __str__(self):
        return self.certificate


class Platform(models.Model):
    platform_name = models.CharField(max_length=20)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'

    def __str__(self):
        return self.platform_name


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_url = models.CharField(max_length=200, blank=True, null=True)
    project_detail = models.TextField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=True, null=True)
    framework = models.ForeignKey(TechFramework, on_delete=models.CASCADE, blank=True, null=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=True, null=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.technology.name
        