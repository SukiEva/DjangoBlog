
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils import timezone
from mdeditor.fields import MDTextField
from apps.users.models import BaseModel, UserProfile

import markdown

# 文章分类
class Category(BaseModel):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def articles(self):
        articles= self.article_set.all()
        return articles


# 文章标签
class Tag(BaseModel):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    body = MDTextField('内容')
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    #img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    author = models.ForeignKey(
        UserProfile,
        verbose_name='作者',
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    views = models.PositiveIntegerField('阅读量', default=0)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={
            'article_id': self.id,
        })

    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])

    # @property
    # def toc(self):
    #     return self.rich_content.get("toc", "")

    @property
    def body_html(self):
        return self.rich_content.get("body", "")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)


def generate_rich_content(value):
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    body = md.convert(value)
    # toc = md.toc
    return {'body': body }

# 留言
class MessageBoard(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱', blank=True)
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])

