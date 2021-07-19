from django.db.models import Count

from .models import *

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Add article ', 'url': 'add_article'},
        {'title': 'Contacts', 'url': 'contacts'},
        {'title': 'About', 'url': 'about'},
        {'title': 'Login', 'url': 'login'}
    ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()

        if 'category_selected' not in context:
            context['category_selected'] = 0

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        return context
