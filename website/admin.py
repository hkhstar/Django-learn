from django.contrib import admin
from .models import Contact 
# Register your models here.
class Contactadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name' ,'email','created_date')
    list_filter = ('name',)
    search_fields = ['name','message'] 
    # ordering=['-created_date']
admin.site.register(Contact,Contactadmin)