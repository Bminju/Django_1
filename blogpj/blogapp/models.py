# model 내용 바꼈을 때 migration 해주기 (database 관련)
from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=180)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # string으로 반환하는 python 기본 함수, self(Post)
        return self.title