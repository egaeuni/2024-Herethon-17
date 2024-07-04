from django.db import models
from django.contrib.auth.models import User

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
    created_at = models.DateTimeField(auto_now_add=True)  #최신 등록순

    def __str__(self):
        return self.title

class Benefit(models.Model):
    policy = models.ForeignKey(Policy, related_name='benefits', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    eligibility = models.TextField(blank=True, null=True)  # 지원 조건
    application_period = models.TextField(blank=True, null=True)  # 신청 시기
    application_method = models.TextField(blank=True, null=True) #신청 방법
    additional_info = models.TextField(blank=True, null=True)  # 기타
    planned_changes = models.TextField(blank=True, null=True) #개편 예정

    def __str__(self):
        return self.title

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, related_name='scraps', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.policy.title}"