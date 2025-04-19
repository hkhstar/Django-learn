from website.views import *
from django.urls import path


urlpatterns = [
    
    path('',index_view),
    path('contact',contact_view),
    path('about',about_view)

]