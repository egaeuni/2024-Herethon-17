from django.db import models
from django.contrib.auth.models import User

class Mento(models.Model):
    name = models.CharField(max_length=50)
    intro = models.TextField()
    content_1 = models.CharField(max_length=150)
    content_2 = models.CharField(max_length=150, null=True, blank=True)
    content_3 = models.CharField(max_length=150, null=True, blank=True)
    content_4 = models.CharField(max_length=150, null=True, blank=True)
    time = models.TextField(null=True, blank=True)
    nickname = models.CharField(max_length=100)
    tag = models.TextField()

    def __str__(self):
        return self.name

class Record(models.Model):
    plan = models.TextField(null=True, blank=True)
    advice = models.TextField(null=True, blank=True)
    pledge = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # 사용자 필드

class Question(models.Model):
    content = models.TextField()
    mento = models.ForeignKey(to=Mento, on_delete=models.CASCADE, related_name='questions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # 사용자 필드

    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.TextField()
