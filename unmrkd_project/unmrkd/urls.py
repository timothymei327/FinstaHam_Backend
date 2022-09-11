from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForumList.as_view(), name='forum_list'),
    path('forums/<int:pk>', views.ForumDetail.as_view(), name='forum_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]