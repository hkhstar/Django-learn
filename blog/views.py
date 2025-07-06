from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

now=timezone.now()
def blog_home(request,**kwargs):
    posts = post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')
    if kwargs.get('cat_name')!=None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!= None:
        posts = posts.filter(author__username=kwargs['author_username'])

    posts=Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        


    contexts={'posts':posts}
    return render(request,'blog/blog-home.html',contexts)



def blog_single(request,pid):
    posts=get_object_or_404(post,published_date__lte=now,pk=pid,status=1)

    posts.counted_views += 1
    posts.save(update_fields=['counted_views'])

    next_post = post.objects.filter(id__gt=posts.id,published_date__lte=now, status=True).order_by('id').first()
    prev_post = post.objects.filter(id__lt=posts.id,published_date__lte=now, status=True).order_by('-id').first()
    context={'post':posts,'next':next_post,'prev':prev_post}
    return render(request,'blog/blog-single.html',context)


def blog_search(request):
    posts = post.objects.filter(published_date__lte=now,status=True)
    if request.method=="GET":
        print(request.GET.get('s'))
        if s :=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    contexts={'posts':posts}
    return render(request,'blog/blog-home.html',contexts)
# def blog_category(request,cat_name):
    
#     posts = post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')
#     posts = posts.filter(category__name=cat_name)
#     contexts={'posts':posts}
#     return render(request,'blog/blog-home.html',contexts)


# def test(request,pid):
#     posts=get_object_or_404(post,pk=pid)
#     context={'post':posts}
#     return render(request,'test.html',context)

# Create your views here.
