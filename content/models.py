from django.db import models

# Create your models here.

#피드
class Feed(models.Model):
    content = models.TextField() #글내용
    image = models.TextField()   # 피드 이미지
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)

#좋아요
class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)
    is_like = models.BooleanField(default=True) #좋아요 선택시 Y

#댓글
class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)
    reply_content = models.TextField()

#북마크
class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)
    is_marked = models.BooleanField(default=True)