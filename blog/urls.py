from blog.views import *
from django.urls import path

app_name='blog'

urlpatterns = [
    
    path('',blog_home,name='index'),
    path('blog',blog_single,name='single'),
    

]