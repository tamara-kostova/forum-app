from django.urls import path, re_path
from .views import index, PostListView, PostDetailView, CommentListView, TestTemplateView
from forum.forum_feeds import LatestPostsFeed

urlpatterns = [
    path('', index, name='index'),
    path('latest/posts/', LatestPostsFeed()),
    path('test', TestTemplateView.as_view(), name='template'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:post_id>/comment/', CommentListView.as_view(), name='comment'),
    re_path(r'^posts/(?P<year>[0-9]{4})/$', PostListView.as_view(), name='by_year'),
    re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', PostListView.as_view(), name='by_month'),
    # re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', 'views.post_detail', 'slug_detail')
]
