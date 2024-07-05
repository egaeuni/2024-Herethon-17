from django.db import models
from datetime import date
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # 파일을 업로드할 경로를 결정하는 함수
    return 'profile_pics/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(default=date(2000, 1, 1))
    profile_pic = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    nickname = models.CharField(max_length=100, default='User')  # 닉네임 필드 추가

    def __str__(self):
        return self.user.username
