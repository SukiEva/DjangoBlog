from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
import xadmin
from apps.blogs.feeds import AllPostsRssFeed


urlpatterns = [
    # 后台管理
    path('xadmin/', xadmin.site.urls),
    # 博客主要功能 url
    re_path(r'', include('apps.blogs.urls', namespace='blogs')),
    # markdown编辑
    re_path(r'mdeditor/', include('mdeditor.urls')),
    # 评论功能 url
    # path('', include('apps.comments.urls', namespace='comments')),
    # 上传图片url设置
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # RSS订阅
    path('all/rss/', AllPostsRssFeed(), name='rss'),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
