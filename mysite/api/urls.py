from django.urls import path
from .import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
    path('myblogposts/', views.UserBlogPost.as_view(), name='my-blogpost'),
    path('all/blogposts/', views.BlogPostList.as_view(), name='all'),
]

