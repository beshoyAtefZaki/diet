# 
from .models import (FoodTable    ,
					 FoodGroup    , 
					 HomeStandard , 
					 Choises      ,
					 ItemGroup    , 
					 Unit , Meals)
from django.contrib import admin





class FoodTableAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_arabic_name','item_group','enerygy' ,'protein','fat','Carbohydrate' )
    list_filter = ['item_group' ]
    search_fields = ['item_name', 'item_arabic_name']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset 
        return queryset, use_distinct


# class HomeStandardAdmin(admin.ModelAdmin):
# 	list_display = ('unit_name' , 'item_group ' , 'enerygy' )
# Register your models here.
admin.site.register(FoodTable )
admin.site.register(FoodGroup)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('description' ,'item', 'home_standrd_wieght','item_group' , 'enerygy' )
    list_filter = ('item_group' , 'item' )
    search_fields = ['description']
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset 
        return queryset, use_distinct

# admin.site.register(HomeStandard,HomeStandardAdmin)
admin.site.register(Choises)
admin.site.register(Unit,UnitAdmin )
admin.site.register(ItemGroup)
admin.site.register(Meals)