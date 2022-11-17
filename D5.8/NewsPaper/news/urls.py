from django.urls import path
from .views import PostList, PostDetail, SearchList, CreateNews, UpdateNews, PostDelete

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('', PostList.as_view()),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('news/search/', SearchList.as_view(), name='search_list'),
    path('news/create/', CreateNews.as_view(), name='create_news'),
    path('news/<int:pk>/update/', UpdateNews.as_view(), name='update_news'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),


]
