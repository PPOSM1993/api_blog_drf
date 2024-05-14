from django.urls import path
from . import views

urlpatterns = [
    path('blog_post/', views.BlogPostCreateView.as_view(), name='blog_post'),
    path('blog_post/<int:pk>/', views.BlogPostRetrieveUpdate.as_view(), name='update_blog_post')
]
