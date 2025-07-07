from django.utils import timezone
from django import template
from blog.models import post
from blog.models import Category    
register = template.Library()

@register.inclusion_tag('blog/blog-latespost.html')
def lates_p(arg=3):
    posts=post.objects.filter(published_date__lte=timezone.now(),status=True).order_by('-published_date')[:arg]
    return {'posts': posts}





@register.inclusion_tag('blog/blog-category.html')
def category_p():
    posts=post.objects.filter(published_date__lte=timezone.now(),status=True)
    category_posts=Category.objects.all
    post_cat=dict()
    for cat in category_posts():
        post_cat[cat] = posts.filter(category=cat).count()
    return {'categories': post_cat}