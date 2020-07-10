from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.blogs.models import Article, Category, MessageBoard

import markdown
import re

class IndexView(generic.ListView):
    '''
    主页
    '''
    template_name = 'blog/index.html'
    paginate_by = 5
    object = Article

    def get(self, request, *args, **kwargs):
        lists = Article.objects.all()

        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(lists, 5, request=request)
        articles = p.page(page)
        return render(request, "blog/index.html", {
            "lists": articles
        })


class ArchiveView(generic.ListView):
    '''
    归档
    '''
    template_name = 'blog/archives.html'

    def get(self, request, *args, **kwargs):
        all_articles = Article.objects.all()
        return render(request, "blog/archives.html", {
            "all_articles": all_articles
        })


def ArticleDetailView(request, article_id):
    '''
    文章内容
    '''
    post = get_object_or_404(Article, id=article_id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    return render(request, 'blog/detail.html', context={'post': post})





class CategoryView(generic.ListView):
    """
    文章分类
    """

    def get(self, request, *args, **kwargs):
        all_categories = Category.objects.all().order_by('index')
        return render(request, 'blog/categories.html', locals())


def MessageForm(request):

    if request.method == "POST":
        comment = MessageBoard()
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        url = request.POST.get("url", "")
        text = request.POST.get("text", "")
        comment.name = name
        comment.email = email
        comment.url = url
        comment.text = text
        comment.save()
        return HttpResponseRedirect('/commentsboard/')

    if request.method == "GET":
        all_messages = MessageBoard.objects.all().order_by('created_time')
        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        p = Paginator(all_messages, 10, request=request)
        comments = p.page(page)
        return render(request, "blog/commentsboard.html", {
            "all_messages": comments,
            "Total":all_messages
        })
