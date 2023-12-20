from django.contrib import admin

from electronics_sales.models import Factory, RetailNetwork, IndividualEntrepreneur


# Register your models here.

@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'title_product', 'time_create')
    list_filter = ('city',)


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'title_product', 'time_create', 'debt', 'provider')
    list_filter = ('city',)


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'title_product', 'product_launch_date', 'time_create', 'debt', 'provider')
    list_filter = ('city',)
