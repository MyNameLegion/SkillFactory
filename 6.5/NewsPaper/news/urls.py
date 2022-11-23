from django.urls import path
from .views import PostList, PostDetail, SearchList, CreateNews, UpdateNews, PostDelete, CategoryList, subscribe, \
    unsubscribe

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('', PostList.as_view()),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('news/search/', SearchList.as_view(), name='search_list'),
    path('news/create/', CreateNews.as_view(), name='create_news'),
    path('news/<int:pk>/update/', UpdateNews.as_view(), name='update_news'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/categories/<int:pk>/', CategoryList.as_view(), name='category_list'),
    path('news/categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('news/categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]
