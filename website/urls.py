from website.views import *
from django.urls import path


urlpatterns = [
    
    path('',index_view),
    path('index.html',index_view),
    path('contact.html',contact_view),
    path('about.html',about_view)

]