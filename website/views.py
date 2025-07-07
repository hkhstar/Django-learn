from django.shortcuts import render
from blog.models import post
from django.utils import timezone
# from django.http import HttpResponse 


# # Create your views here.

# def index_view(request):
#     return HttpResponse('<h1>home</h1>')

# def contact_view(request):
#     return HttpResponse('<h1>contact</h1>')


# def about_view(request):
#     return HttpResponse('<h1>about</h1>')



now=timezone.now()


def index_view(request):
    posts = post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')
    contexts={'posts':posts[:6]}
    return render(request,'website/index.html',contexts)


def contact_view(request):
    return render(request,'website/contact.html')

def about_view(request):
    return render(request,'website/about.html')
# def test_view(request):
#     context={"name":"Hamoun","lastname":"Khatirzad"}
#     return render(request,'website/test.html',context)