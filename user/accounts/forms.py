from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'nickname']
        labels = {
            'profile_pic': '',  # 필드 레이블 제거
            'nickname': '닉네임'  # 닉네임 필드 레이블 추가
        }
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'file-upload'}),
            'nickname': forms.TextInput(attrs={'class': 'nickname-input'})  # 닉네임 필드에 클래스 추가
        }
