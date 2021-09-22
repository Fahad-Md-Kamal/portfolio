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
    icon = models.CharField(max_length=50, help_text='Get Embaded HTML url from www.icons8.com')
    title = models.CharField(max_length=20)
    serial = models.IntegerField(default=0)
    description = models.TextField(max_length=100)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['serial']

    def __str__(self):
        return self.title


SKILL_CATEGORIES = [
    (1, 'LANGUAGE'),
    (2, 'FRAMEWORK'),
    (3, 'ADDITIONAL'),
]


class Skill(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=SKILL_CATEGORIES, default=1)
    efficiency = models.DecimalField(max_digits=3, decimal_places=1)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['-efficiency']

    def __str__(self):
        return self.name


EDU_TYPE = [
    (1, 'ACADEMIC'),
    (2, 'CERTIFICATE'),
]


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=100)
    organization = models.CharField(max_length=50)
    edu_type = models.IntegerField(choices=EDU_TYPE, default=1)
    passing_year = models.IntegerField()
    achieved_cgpa = models.CharField(max_length=10)
    base_cgpa = models.CharField(max_length=10, default=5.00)
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
    technology = models.ForeignKey(
        Technology, on_delete=models.CASCADE, blank=True, null=True)
    platform = models.ForeignKey(
        Platform, on_delete=models.CASCADE, blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name
