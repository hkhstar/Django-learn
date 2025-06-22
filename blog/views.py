from django.shortcuts import render
from blog.models import post



def blog_home(request):
    
    posts=post.objects.filter(status=1)
    contexts={'posts':posts}
    return render(request,'blog/blog-home.html',contexts)
def blog_single(request):
    return render(request,'blog/blog-single.html')


# Create your views here.
