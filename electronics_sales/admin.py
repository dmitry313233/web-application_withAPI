from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from electronics_sales.models import Factory, RetailNetwork, IndividualEntrepreneur


# Register your models here.


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'title_product', 'time_create', 'debt')
    list_filter = ('city',)
    actions = ['debt_clearer']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def debt_clearer(self, request, gs: QuerySet):
        gs.update(debt=0)
        self.message_user(request,
                          "Были очищены задолжности у выбранных объектов")


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'title_product', 'time_create', 'debt', 'provider_url')
    list_filter = ('city',)
    actions = ['debt_clearer']

    def provider_url(self, obj):
        url = reverse("admin:electronics_sales_factory_change", args=[obj.provider.id])  # electronics_sales это название приложения, factory это то модель на ссылку, change - не меняемое
        return format_html('<a href="{}">{}</a>', url, obj.provider.name)

    provider_url.short_description = 'Поставщик'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def debt_clearer(self, request, qs: QuerySet):
        qs.update(debt=0)
        self.message_user(request,
                          "Были очищены задолженности у выбранных объектов.")


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'title_product', 'product_launch_date', 'time_create', 'debt', 'provider_url')
    list_filter = ('city',)
    actions = ['debt_clearer']

    def provider_url(self, obj):
        if obj.provider:
            url = reverse("admin:electronics_sales_retailnetwork_change", args=[obj.provider.id])
            return format_html('<a href="{}">{}</a>', url, obj.provider.name)
        else:
            url = reverse("admin:electronics_sales_factory_change", args=[obj.factory.id])
            return format_html('<a href="{}">{}</a>', url, obj.factory.name)

    provider_url.short_description = 'Поставщик'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def debt_clearer(self, request, qs: QuerySet):
        qs.update(debt=0)
        self.message_user(request,
                      "Были очищены задолженности у выбранных объектов.")
