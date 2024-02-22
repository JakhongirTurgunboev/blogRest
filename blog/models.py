import time

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_to(instance, filename):
    return f'images/{filename}'


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Blog)
def update_blog(sender, instance, **kwargs):
    word1 = "salom"
    time.sleep(2)
    if word1 in instance.title or instance.text:
        instance.delete()


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.author}'


class Like(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog}'
