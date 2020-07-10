import xadmin

from apps.theme.models import HomePage

class HomePageAdmin(object):
    list_display = ['title', 'home_title', 'home_title_down', 'nick_name', 'introduction']

xadmin.site.register(HomePage, HomePageAdmin)

