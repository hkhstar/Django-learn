from django.shortcuts import render,get_object_or_404
from blog.models import post



def blog_home(request):
    
    posts=post.objects.filter(status=1)
    contexts={'posts':posts}
    return render(request,'blog/blog-home.html',contexts)
def blog_single(request):
    return render(request,'blog/blog-single.html')
def test(request,pid):
    posts=get_object_or_404(post,pk=pid)
    context={'post':posts}
    return render(request,'test.html',context)

# Create your views here.
