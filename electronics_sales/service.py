from django_filters import rest_framework as filters

from electronics_sales.models import Factory, RetailNetwork, IndividualEntrepreneur


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FactoryFilter(filters.FilterSet):
    search = CharFilterInFilter(field_name='search__country', lookup_expr='in')

    class Meta:
        model = Factory
        fields = ['country']


class RetailNetworkFilter(filters.FilterSet):
    search = CharFilterInFilter(field_name='search__country', lookup_expr='in')

    class Meta:
        model = RetailNetwork
        fields = ['country']


class IndividualEntrepreneurFilter(filters.FilterSet):
    search = CharFilterInFilter(field_name='search__country', lookup_expr='in')

    class Meta:
        model = IndividualEntrepreneur
        fields = ['country']
