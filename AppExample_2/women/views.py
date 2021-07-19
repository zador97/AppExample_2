from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


# def home(request):
#     posts = Women.objects.all()
#
#     context = {
#         'title': 'Home',
#         'posts': posts,
#         'category_selected': 0
#     }
#     return render(request, 'women/home.html', context=context)


# @login_required
# декоратор для ограницения неавторизованного пользователя
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'women/about.html', context=context)


def categories(request, cat_id):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)

    return HttpResponse(f"categories: {cat_id}")


def archive(request, year):
    # if int(year) > 2020:
    #     raise Http404()
    if int(year) > 2020:
        return redirect('index', permanent=False)

    return HttpResponse(f"archive year: {year}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h2>Not found</h2>")


# def add_article(request):
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddArticleForm()
#
#     context = {
#         'form': form,
#         'title': 'Add article'
#     }
#     return render(request, 'women/add_article.html', context=context)


def contacts(request):
    posts = Women.objects.all()
    context = {
        'title': 'Contacts',
        'posts': posts
    }
    return render(request, 'women/contacts.html', context=context)


def login(request):
    posts = Women.objects.all()
    context = {
        'title': 'Login',
        'posts': posts
    }

    return render(request, 'women/login.html', context=context)


# def article(request, article_slug):
#     article = get_object_or_404(Women, slug=article_slug)
#
#     context = {
#         'title': 'Article',
#         'article': article,
#         'category_selected': article.category_id
#     }
#     return render(request, 'women/article.html', context=context)


# def category(request, category_slug):
#     category = Category.objects.get(slug=category_slug)
#     posts = Women.objects.filter(category_id=category.id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'title': 'Category',
#         'posts': posts,
#         'category_selected': category.id
#     }
#     return render(request, 'women/category.html', context=context)


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/home.html'
    context_object_name = 'posts'

    # extra_context = {  # только статика
    #     'title': 'Home'
    # }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


class ShowArticle(DataMixin, DetailView):
    model = Women
    template_name = 'women/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['article'], category_selected=context['article'].category_id)

        return dict(list(context.items()) + list(c_def.items()))


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/home.html'
    context_object_name = 'posts'
    allow_empty = False  # исключение - 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].category), category_selected=context['posts'][0].category_id)

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class AddArticle(LoginRequiredMixin, DataMixin, CreateView):
    login_url = reverse_lazy('home')  # редирект не авторизованного пользователя
    raise_exception = True  # ошибка для не авторизованного пользователя

    form_class = AddArticleForm
    template_name = 'women/add_article.html'
    success_url = reverse_lazy('home')  # редирект после добавления

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add article')

        return dict(list(context.items()) + list(c_def.items()))
