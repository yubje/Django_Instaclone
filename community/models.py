from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 원본 그대로
    image = models.ImageField()
    # DB 저장 X, 호출하게되면, 잘라서 표현
    image_thumbnail = ImageSpecField(source='image',
                          processors=[Thumbnail(300, 300)],
                          format='JPEG',
                          options={'quality': 60})

    # 원본 잘라서 저장 : ProcessedImageField
    # image = ProcessedImageField(
    #                       processors=[ResizeToFill(100, 50)],
    #                       format='JPEG',
    #                       options={'quality': 60})

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles'
    )

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
