from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):

    profile_image = models.TextField()# 프로필 이미지
    nickname = models.CharField(max_length=24, unique=True) #닉네임
    name = models.CharField(max_length=24) #이름
    email = models.EmailField(unique=True) #이메일

    USERNAME_FIELD = 'nickname'

    class Meta: #테이블 이름을 정함
        db_table="User"
