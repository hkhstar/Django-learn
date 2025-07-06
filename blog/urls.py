from blog.views import *
from django.urls import path

app_name='blog'

urlpatterns = [
    
    path('',blog_home,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_home,name='category'),
    # path('category/<str:cat_name>',blog_category,name='category'),
    path('author/<str:author_username>',blog_home,name='author'),
    path('search/',blog_search,name='search'),
    # path('post-<int:pid>',test,name='test'),
  
]