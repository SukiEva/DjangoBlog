
from apps.theme.models import HomePage

def global_settings(request):
    var_dict = {}
    all_messages = HomePage.objects.all()
    if all_messages:
        message = all_messages[0]
        var_dict = {
            "message": message
        }
    return var_dict


