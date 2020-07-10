from django.db import models

from django.db import models

# 主页
class HomePage(models.Model):
    CHECK_CHOICES = (
        ('o', '打开'),
        ('c', '关闭'),
    )
    title = models.CharField("站点标题", max_length=20, default="welcome")
    home_title = models.CharField('主页标题', max_length=20, default='DjangoBlog')
    home_title_down = models.CharField('主页副标题', max_length=20, default='use Theme NextT')
    nick_name = models.CharField('昵称', max_length=20, default="username")
    head_image = models.ImageField(verbose_name="用户头像(≤512x512)", upload_to="head_image")
    introduction = models.CharField('简介', max_length=50, default="hello world")
    email = models.EmailField('邮箱', max_length=50, blank=True, null=True)
    github = models.CharField('Github 用户名', max_length=20, blank=True, null=True)
    csdn = models.CharField('CSDN ID号', max_length=100, blank=True, null=True)
    beian = models.CharField('备案号', max_length=100, default="", blank=True, null=True)
    music = models.CharField('网易云歌曲 ID', max_length=20, default="28692687")
    live2d = models.CharField(
        'live2d开启',
        max_length=1,
        choices=CHECK_CHOICES,
        default='c')


    class Meta:
        verbose_name = "主题配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.home_title

