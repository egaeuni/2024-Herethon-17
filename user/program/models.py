from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=200)
    center_info = models.CharField(max_length=200, blank=True, null=True)
    event_period = models.CharField(max_length=200, blank=True, null=True)
    registration_period = models.CharField(max_length=200, blank=True, null=True)
    participants = models.CharField(max_length=200, blank=True, null=True)
    event_content = models.TextField(blank=True, null=True)
    session_info = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=100)
    image = models.ImageField(upload_to='program_images/', blank=True, null=True)
    application_url = models.URLField(max_length=200, blank=True, null=True)  # 신청 URL 필드 추가

    def __str__(self):
        return self.title

class Policy(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Benefit(models.Model):
    policy = models.ForeignKey(Policy, related_name='benefits', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    application_method = models.TextField()
    planned_changes = models.TextField()

    def __str__(self):
        return self.title
