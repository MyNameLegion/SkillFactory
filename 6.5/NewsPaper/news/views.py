from datetime import datetime, timedelta
from django.utils import timezone
import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .filters import PostFilter
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post, Category
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = 'date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        user = self.request.user
        limit = 3
        today = timezone.now()
        prev_day = today - timedelta(days=1)
        posts_day_count = Post.objects.filter(date_time__gte=prev_day, author__authorUser=user).count()
        context['posts_limit'] = limit <= posts_day_count
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class SearchList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CreateNews(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'create_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        limit = 5
        today = timezone.now()
        prev_day = today - timedelta(days=1)
        posts_day_count = Post.objects.filter(date_time__gte=prev_day, author__authorUser=user).count()
        print(posts_day_count)
        print(limit)
        context['posts_limit'] = limit <= posts_day_count
        return context


class UpdateNews(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'create_news.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CategoryList(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required()
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})


@login_required()
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'Вы отписались от рассылки'
    return render(request, 'news/unsubscribe.html', {'category': category, 'message': message})


