from django.contrib.auth.models import AbstractUser
from django.db import models

DEFAULT_MAX_LENGTH = 64


# Create your models here.
class User(AbstractUser):
    AUTHOR = 1
    COMMENTATOR = 2

    ROLE_CHOICES = (
        (AUTHOR, 'Author'),
        (COMMENTATOR, 'Commentator'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('Comment', on_delete=models.PROTECT)
    text = models.TextField()

    def __str__(self):
        return f'{self.id}| {self.post} {self.parent_comment}'
