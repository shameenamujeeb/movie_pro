from .models import Category,Movie

def menu_links(request):
    link_s=Category.objects.all()

    return dict(links=link_s)


