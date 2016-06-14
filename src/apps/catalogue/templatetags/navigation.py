from django import template
from src.apps.catalogue.models import Category

register = template.Library()


class MenuNode(template.Node):
    def __init__(self):
        pass

    def render(self,
               context):
        context = Category.objects.all()
        return context


def render_menu(parser,
                token):
    return MenuNode()

register.tag('navigation',
             render_menu)

