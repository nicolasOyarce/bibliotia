from .models import Category


def menu_links(request):
    """
    Context processor for the menu links
    """
    links = Category.objects.all()
    return dict(links=links)