from django.contrib import admin
from .models import product,brand , color , category

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'categories',"date",'brands','colors']
    search_fields = ['name','price','categories__subcategory',"date",'colors__colores','brands__brandes']
    list_filter = ('categories__subcategory','colors__colores','brands__brandes')
    


admin .site.register(product,productAdmin)
admin .site.register(category)
admin .site.register(color)
admin .site.register(brand)
