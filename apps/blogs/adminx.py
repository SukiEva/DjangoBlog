import xadmin

from apps.blogs.models import Article, Tag, Category, MessageBoard




class ArticleAdmin(object):
    list_display = ['title', 'author', 'category', 'tags', 'created_time', 'modified_time', 'views']
    search_fields = ['title']
    list_filter = ['category', 'tags', 'created_time', 'modified_time']
    list_editable = ['title', 'categoty']
    filter_horizontal= ('tags',)

xadmin.site.register(Article, ArticleAdmin)

class TagAdmin(object):
    search_fields = ['name']
    list_filter = ['name']

xadmin.site.register(Tag, TagAdmin)

class CategoryAdmin(object):
    list_display = ['name', 'index']
    search_fields = ['name', 'index']
    list_filter = ['name', 'index']
    list_editable = ['name', 'index']

xadmin.site.register(Category, CategoryAdmin)

class MessageBoardAdmin(object):
    list_display = ['name', 'email', 'url', 'created_time']

xadmin.site.register(MessageBoard, MessageBoardAdmin)
