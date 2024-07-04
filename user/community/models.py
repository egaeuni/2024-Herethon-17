# community/models.py
from django.db import models
from django.contrib.auth.models import User  # Django 기본 User 모델 사용

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="liked_posts")
    scrap = models.ManyToManyField(to=User, through="Scrap", related_name="scraped_posts")

    def __str__(self):
        return f'[{self.id}] {self.title}'

class Answer(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="answers")
    content= models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return f'[{self.id}] {self.content}'

class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")

class Scrap(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_scraps")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_scraps")

    def __str__(self):
        return f'[{self.id}] {self.title}'
