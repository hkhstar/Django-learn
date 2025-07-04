from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone

now=timezone.now()
def blog_home(request):
    
    posts = post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')
    contexts={'posts':posts}
    return render(request,'blog/blog-home.html',contexts)



def blog_single(request,pid):
    posts=get_object_or_404(post,pk=pid,status=1)

    posts.counted_views += 1
    posts.save(update_fields=['counted_views'])

    next_post = post.objects.filter(id__gt=posts.id,published_date__lte=now, status=True).order_by('id').first()
    prev_post = post.objects.filter(id__lt=posts.id,published_date__lte=now, status=True).order_by('-id').first()
    context={'post':posts,'next':next_post,'prev':prev_post}
    return render(request,'blog/blog-single.html',context)


# def test(request,pid):
#     posts=get_object_or_404(post,pk=pid)
#     context={'post':posts}
#     return render(request,'test.html',context)

# Create your views here.
