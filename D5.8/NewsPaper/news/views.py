from datetime import datetime

from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .filters import PostFilter
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post, Comment
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

