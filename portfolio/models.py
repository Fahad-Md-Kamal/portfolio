from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile/')
    gmail = models.EmailField(null=True, blank=True)
    slug = models.SlugField(max_length=255)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contacts_set')
    contact= models.CharField(max_length=20)
    serial = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.name}\'s {self.contact}'
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['serial']

class Email(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='emails_set')
    email= models.CharField(max_length=255)
    serial = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.name}\'s {self.email}'
    
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        ordering = ['serial']

class  OtherURLS(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='url_profile')
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'OtherURLS'
        verbose_name_plural = 'OtherURLS'

    def save(self, *args, **kwargs):
        if self.email != None and self.url != None:
            raise ValueError('Email and URL both cannot be accepted at a time.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



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
    icon = models.CharField(
        max_length=50, help_text='Get Embaded HTML url from www.icons8.com')
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
    serial_num = models.IntegerField(
        default=0, help_text="This is order the projects heirarcy.")
    project_url = models.CharField(max_length=200, blank=True, null=True)
    project_detail = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='projects/')
    technology = models.ForeignKey(
        Technology, on_delete=models.CASCADE, blank=True, null=True)
    platform = models.ForeignKey(
        Platform, on_delete=models.CASCADE, blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['serial_num']

    def __str__(self):
        return self.project_name
