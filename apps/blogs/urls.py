from django.urls import path, re_path

from . import views

app_name = "blogs"
urlpatterns = [
    # 首页
    path(
        r'',
        views.IndexView.as_view(),
        name='index'
    ),
    # 文章内容
    path(
        r'article/<int:article_id>',
        views.ArticleDetailView,
        name = 'detail'
    ),
    # 归档
    path(
        r'archives/',
        views.ArchiveView.as_view(),
        name = 'archives'
     ),
    # 分类
    path(
        r'categories/',
        views.CategoryView.as_view(),
        name = 'categories'
    ),
    # 留言板
    path(
        r'commentsboard/',
        views.MessageForm,
        name='board')
]
