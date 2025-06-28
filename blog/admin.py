from django.contrib import admin
from .models import post
# Register your models here.
@admin.register(post)
class postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author','counted_views','status','published_date','created_date')
    list_filter = ('status','author')
    search_fields = ['title','content'] 
    # ordering=['-created_date']

# admin.site.register(post,postadmin)

