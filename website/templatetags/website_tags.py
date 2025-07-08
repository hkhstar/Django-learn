from django.utils import timezone
from django import template
from blog.models import post
  
register = template.Library()


@register.inclusion_tag('website/tags/website_latestpost.html')
def lastest_p():
    lastest = post.objects.filter(published_date__lte=timezone.now(),status=True).order_by('-published_date')
    return {'lastest':lastest[:6]}