from django.contrib import admin
from testapp.models import Beer
# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_Display=['name','taste','color','price']

admin.site.register(Beer,BeerAdmin)    
