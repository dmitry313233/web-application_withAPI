from django.urls import path
from rest_framework.routers import DefaultRouter

from electronics_sales.apps import ElectronicsSalesConfig
from electronics_sales.views import FactoryCreateListAPIView, FactoryView, RetailNetworkCreateListAPIView, \
    RetailNetworkView, IndividualEntrepreneurCreateListAPIView, IndividualEntrepreneurView

app_name = ElectronicsSalesConfig.name

router = DefaultRouter()

urlpatterns = [
    path('factory_create_list/', FactoryCreateListAPIView.as_view(), name='factory_create_list'),
    path('factoryView/<int:pk>/', FactoryView.as_view(), name='FactoryView'),

    path('retailnetwork_create_list/', RetailNetworkCreateListAPIView.as_view(), name='retailnetwork_create_list'),
    path('retailnetworkView/<int:pk>/', RetailNetworkView.as_view(), name='retailnetworkView'),

    path('individuale_create_list/', IndividualEntrepreneurCreateListAPIView.as_view(), name='individuale_create_list'),
    path('individualntrepreneurView/<int:pk>/', IndividualEntrepreneurView.as_view(), name='individualntrepreneurView')

] + router.urls
