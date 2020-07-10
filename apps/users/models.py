from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True




class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username

