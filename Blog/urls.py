from django.urls import path
from Blog.views import BlogListView, activity, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('view/<int:pk>/<slug:slug>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('activity/<int:pk>/', activity, name='activity'),
]