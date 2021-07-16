from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        categories_list = Category.objects.all()
    else:
        categories_list = Category.objects.filter(id=filter)

    return categories_list


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categorys_list = Category.objects.all()
    else:
        categorys_list = Category.objects.order_by(sort)

    return { "categorys_list": categorys_list, 'category_selected': category_selected }


@register.inclusion_tag('women/menu.html')
def show_menu():
    menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Add article ', 'url': 'add_article'},
        {'title': 'Contacts', 'url': 'contacts'},
        {'title': 'About', 'url': 'about'},
        {'title': 'Login', 'url': 'login'}
    ]

    return {'menu': menu}

