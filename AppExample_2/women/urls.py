from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    # path('', cache_page(60)(WomenHome.as_view()), name='home'),  - кэширование
    path('', WomenHome.as_view(), name='home'),                                    # адрес с модом
    path('about/', about, name='about'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('contacts/', FeedbackFormView.as_view(), name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),     # адрес с переменной slug
    path('category/<slug:category_slug>/', WomenCategory.as_view(), name='category'),     # адрес с переменной slug
    path('categories/<int:cat_id>/', categories, name='categories'),     # адрес с переменной int
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive')    # адрес с регуляркой
]
