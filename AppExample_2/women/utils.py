from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [
        {'title': 'Home', 'url': 'home'},
        {'title': 'Add article ', 'url': 'add_article'},
        {'title': 'Contacts', 'url': 'contacts'},
        {'title': 'About', 'url': 'about'}
    ]


class DataMixin:
    paginate_by = 50

    def get_user_context(self, **kwargs):
        context = kwargs

        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.all()
            cache.set('categories', categories, 60)

        context['categories'] = categories

        if 'category_selected' not in context:
            context['category_selected'] = 0

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        return context
