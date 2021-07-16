from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),                                    # адрес с модом
    path('about/', about, name='about'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),     # адрес с переменной slug
    path('category/<slug:category_slug>/', WomenCategory.as_view(), name='category'),     # адрес с переменной slug
    path('categories/<int:cat_id>/', categories, name='categories'),     # адрес с переменной int
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive')    # адрес с регуляркой
]
